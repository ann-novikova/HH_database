from src.file_worker import JsonWorker
import psycopg2
from src.parser import HeadHunterAPI, HHEmployers
from src.dbmanager import DBManager
from pprint import pprint

from src.database import data_file_path, create_tables, fill_tables

# Параметры подключения к БД
DB_NAME = "hh_vacancies"
DB_USER = "postgres"
DB_PASSWORD = "12345"
DB_HOST = "localhost"

if __name__ == "__main__":
    hh_api = HHEmployers()
    hh_employers = hh_api.load_employers()
    hh_api_vacancies = HeadHunterAPI()
    hh_vacancies = hh_api_vacancies.load_vacancies(hh_employers)
    json_worker = JsonWorker()
    json_worker.write_data(hh_vacancies)

    conn = None
    try:
        conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        create_tables(conn)
        fill_tables(conn)
    except psycopg2.Error as e:
        print(f"Ошибка при работе с PostgreSQL: {e}")
    finally:
        if conn is not None:
            conn.close()
    dbworker = DBManager("hh_vacancies", "12345")
    dbworker.connect()
    pprint(dbworker.get_companies_and_vacancies_count())
    pprint(dbworker.get_all_vacancies())
    pprint(dbworker.get_avg_salary())
    pprint(dbworker.get_vacancies_with_higher_salary())
    pprint(dbworker.get_vacancies_with_keyword("официант"))
    dbworker.connection_close()
