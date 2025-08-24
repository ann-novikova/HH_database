from abc import ABC, abstractmethod

import psycopg2


class BaseManager(ABC):
    """Абстрактный метод для всех классов подключений к БД"""

    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def get_companies_and_vacancies_count(self) -> list[tuple]:
        pass

    @abstractmethod
    def get_all_vacancies(self) -> list[tuple]:
        pass

    @abstractmethod
    def get_avg_salary(self) -> list[tuple]:
        pass

    @abstractmethod
    def get_vacancies_with_higher_salary(self) -> list[tuple]:
        pass

    @abstractmethod
    def get_vacancies_with_keyword(self, keyword: str) -> list[tuple] | None:
        pass

    @abstractmethod
    def connection_close(self) -> None:
        pass


class DBManager(BaseManager):
    """Класс работы с БД PostgreSQL"""

    __slots__ = "conn", "dbname", "password", "user", "host", "port", "cur"

    def __init__(
        self, dbname: str, password: str, user: str = "postgres", host: str = "localhost", port: str = "5432"
    ) -> None:
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self) -> None:
        """Соединение с БД"""
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port
            )

        except Exception as err:
            raise ConnectionError(f"Ошибка подключения к БД -> {err}")

    def get_companies_and_vacancies_count(self) -> list[tuple]:
        """получает список всех компаний и количество вакансий у каждой компании."""

        cursor = self.conn.cursor()
        cursor.execute(
            """SELECT company_name, COUNT(*) as count_vacancies FROM employers
            JOIN vacancies USING(employer_id)
            GROUP BY company_name
            ORDER BY count_vacancies DESC
            """
        )
        return cursor.fetchall()

    def get_all_vacancies(self) -> list[tuple]:
        """получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки
        на вакансию."""
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT
            company_name, vacancy_name, salary_from, salary_to, url
            FROM
            vacancies
            JOIN employers USING(employer_id)
            """
        )
        return cursor.fetchall()

    def get_avg_salary(self) -> list[tuple]:
        """получает среднюю зарплату по вакансиям."""

        cursor = self.conn.cursor()
        cursor.execute("""SELECT AVG(salary_from) FROM vacancies""")
        return cursor.fetchall()

    def get_vacancies_with_higher_salary(self) -> list[tuple]:
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        avg_salary = self.get_avg_salary()
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM vacancies WHERE salary_from > {avg_salary[0][0]}")
        return cursor.fetchall()

    def get_vacancies_with_keyword(self, keyword: str) -> list[tuple] | None:
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова."""

        cursor = self.conn.cursor()
        cursor.execute(
            f"""SELECT * FROM vacancies
        WHERE vacancy_name LIKE '%{keyword.lower()}%' OR
        vacancy_name LIKE '%{keyword.title()}%' OR
        vacancy_name LIKE '%{keyword.upper()}%'
"""
        )
        return cursor.fetchall()

    def connection_close(self) -> None:
        """закрывает активное соединение с БД."""

        self.conn.close()
