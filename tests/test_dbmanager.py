from src.dbmanager import DBManager


def test_def_get_companies_and_vacancies_count(db_manager: DBManager) -> None:
    db_manager.connect()
    assert db_manager.get_companies_and_vacancies_count() == (
        [
            ("0.75 GROUP", 20),
            ("1000 ДЛЯ УДОБНОЙ ЖИЗНИ", 13),
            ("1001 Тур", 7),
            ("1000 и одна туфелька", 6),
            ("1001 LABS", 5),
            ("1001pled.ru", 4),
            ("1001 Крепеж", 3),
            ("001KZ (001КЗ)", 3),
            ("0250", 2),
            ("0704", 1),
            ("1000 Свай", 1),
            ("0not1", 1),
            ("0901", 1),
            ("1000 Ибу", 1),
            ("1001 Тур (ООО Оникс)", 1),
            ("062 detail", 1),
            ("0sprava", 1),
            ("1001 чай", 1),
        ]
    )
    db_manager.connection_close()


def test_get_all_vacancies(db_manager: DBManager, all_vacancies: list[tuple]) -> None:
    db_manager.connect()
    assert db_manager.get_all_vacancies() == all_vacancies
    db_manager.connection_close()


def test_get_avg_salary(db_manager: DBManager) -> None:
    db_manager.connect()
    assert db_manager.get_avg_salary() == [(80078.125,)]
    db_manager.connection_close()


def test_get_vacancies_with_higher_salary(db_manager: DBManager, vacancies_with_higher_salary: list[tuple]) -> None:
    db_manager.connect()
    assert db_manager.get_vacancies_with_higher_salary() == vacancies_with_higher_salary
    db_manager.connection_close()


def test_get_vacancies_with_keyword(db_manager: DBManager) -> None:
    db_manager.connect()
    assert db_manager.get_vacancies_with_keyword("python") == []
    db_manager.connection_close()
