import psycopg2
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
data_file_path = BASE_DIR / "data" / "vacancy.json"

# Параметры подключения к БД
DB_NAME = "hh_vacancies"
DB_USER = "postgres"
DB_PASSWORD = "12345"  # Замените на ваш пароль
DB_HOST = "localhost"



def create_tables(conn) -> None:
    """"Функция для создания таблиц"""

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS employers (
                employer_id SERIAL PRIMARY KEY,
                company_name VARCHAR(255) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS vacancies (
                vacancy_id INTEGER PRIMARY KEY,
                employer_id INTEGER REFERENCES employers(employer_id),
                vacancy_name VARCHAR(255) NOT NULL,
                url VARCHAR(255),
                salary_from REAL,
                salary_to REAL,
                description TEXT,
                requirements TEXT
            );
        """)
    conn.commit()


def fill_tables(conn, filename=data_file_path) -> None:
    """Функция для заполнения таблиц данными"""

    with open(filename, 'r', encoding='utf-8') as f:
        vacancies_data = json.load(f)

    with conn.cursor() as cur:
        cur.execute("TRUNCATE TABLE vacancies CASCADE")
        for vacancy in vacancies_data:
            company = vacancy["employer"]
            company_name = company['name']
            vacancy_id = int(vacancy['id'])
            salary = vacancy.get("salary")  # Handle salary being None
            descr = vacancy["snippet"]
            salary_from = None
            salary_to = None
            if salary:
                salary_from = salary.get("from", 0)
                salary_to = salary.get("to", 0)

            # Проверяем, существует ли работодатель
            cur.execute("SELECT employer_id FROM employers WHERE company_name = %s", (company_name,))
            employer = cur.fetchone()

            if employer is None:
                # Если работодателя нет, добавляем его
                cur.execute("INSERT INTO employers (company_name) VALUES (%s) RETURNING employer_id", (company_name,))
                employer_id = cur.fetchone()[0]
            else:
                employer_id = employer[0]

            # Добавляем вакансию
            cur.execute("""
                INSERT INTO vacancies (vacancy_id, employer_id, vacancy_name, url, salary_from, salary_to, description, requirements)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (vacancy_id) DO NOTHING;  -- Игнорируем дубликаты
            """, (
                vacancy_id,
                employer_id,
                vacancy['name'],
                vacancy['url'],
                salary_from,
                salary_to,
                descr['responsibility'],
                descr['requirement']
            ))

    conn.commit()

