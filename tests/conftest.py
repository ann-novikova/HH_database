import pytest

from src.dbmanager import DBManager
from src.file_worker import JsonWorker, data_path
from src.parser import HeadHunterAPI, HHEmployers
from src.vacancy import Vacancy


@pytest.fixture()
def vacancy1() -> Vacancy:
    return Vacancy(
        "122115665",
        "Начинающий макроэкономист",
        "Центральный банк Российской Федерации (Банк России)",
        "https://api.hh.ru/vacancies/122115665?host=hh.ru",
        50000,
        70000,
        "Построение структурных моделей российской экономики",
        "Требования: опыт работы от 3 лет",
    )


@pytest.fixture()
def vacancy2() -> Vacancy:
    return Vacancy(
        "122115666",
        "Python developer",
        "Some company",
        "https://api.hh.ru/vacancies/122115666?host=hh.ru",
        75000,
        100000,
        "Write code",
        "Python knowledge",
    )


@pytest.fixture()
def jsonworker1() -> JsonWorker:
    return JsonWorker("vacancy_test.json")


@pytest.fixture
def init_hh() -> HeadHunterAPI:
    return HeadHunterAPI()


@pytest.fixture
def init_hh_employer() -> HHEmployers:
    return HHEmployers()


@pytest.fixture
def db_manager() -> DBManager:
    return DBManager("hh_vacancies", "12345")


@pytest.fixture()
def path_to_file() -> str:
    return str(data_path / "vacancy_test.json")


@pytest.fixture()
def list_of_vacancies_to_dict() -> list[dict]:
    return [
        {
            "vacancy_id": "122237214",
            "name": "Frontend-разработчик",
            "company": "Облачные Квантовые Технологии",
            "url": "https://api.hh.ru/vacancies/122237214?host=hh.ru",
            "salary_from": 0,
            "salary_to": 0,
            "description": "Разработка пользовательского интерфейса облачной операционной системы.",
            "requirements": "Опыт использования в работе TDD, CI/CD. Опыт работы в Linux, CLI.",
        },
        {
            "vacancy_id": "121380408",
            "name": "Тестировщик ПО",
            "company": "NEXT Contact",
            "url": "https://api.hh.ru/vacancies/121380408?host=hh.ru",
            "salary_from": 50000,
            "salary_to": 70000,
            "description": "Функциональное, регрессионное, интеграционное, smoke-тестирование, приемочное (UAT).",
            "requirements": "Желателен опыт работы с Kubernetes и Docker. Будет плюсом: знание основ автоматизации",
        },
    ]


@pytest.fixture()
def sorted_list_of_vacancies() -> list[dict]:
    return [
        {
            "vacancy_id": "121380408",
            "name": "Тестировщик ПО",
            "company": "NEXT Contact",
            "url": "https://api.hh.ru/vacancies/121380408?host=hh.ru",
            "salary_from": 50000,
            "salary_to": 70000,
            "description": "Функциональное, регрессионное, интеграционное, smoke-тестирование, приемочное (UAT).",
            "requirements": "Желателен опыт работы с Kubernetes и Docker. Будет плюсом: знание основ автоматизации",
        },
        {
            "vacancy_id": "122237214",
            "name": "Frontend-разработчик",
            "company": "Облачные Квантовые Технологии",
            "url": "https://api.hh.ru/vacancies/122237214?host=hh.ru",
            "salary_from": 0,
            "salary_to": 0,
            "description": "Разработка пользовательского интерфейса облачной операционной системы.",
            "requirements": "Опыт использования в работе TDD, CI/CD. Опыт работы в Linux, CLI.",
        },
    ]


@pytest.fixture()
def list_of_vacancies_with_None() -> list[dict]:
    return [
        {
            "vacancy_id": "121380408",
            "name": "Тестировщик ПО",
            "company": "NEXT Contact",
            "url": "https://api.hh.ru/vacancies/121380408?host=hh.ru",
            "salary_from": 50000,
            "salary_to": 70000,
            "description": "Функциональное, регрессионное, интеграционное, smoke-тестирование, приемочное (UAT).",
            "requirements": "Желателен опыт работы с Kubernetes и Docker. Будет плюсом: знание основ автоматизации",
        },
        {
            "vacancy_id": "122237214",
            "name": "Frontend-разработчик",
            "company": "Облачные Квантовые Технологии",
            "url": "https://api.hh.ru/vacancies/122237214?host=hh.ru",
            "salary_from": None,
            "salary_to": None,
            "description": "Разработка пользовательского интерфейса облачной операционной системы.",
            "requirements": "Опыт использования в работе TDD, CI/CD. Опыт работы в Linux, CLI.",
        },
    ]


@pytest.fixture()
def list_of_vacancies() -> list[dict]:
    return [
        {
            "accept_incomplete_resumes": False,
            "accept_temporary": False,
            "address": {
                "building": "53/1",
                "city": "Новосибирск",
                "description": None,
                "id": "2792399",
                "lat": 55.039863,
                "lng": 82.9358,
                "metro": {
                    "lat": 55.043634,
                    "line_id": "53",
                    "line_name": "Дзержинская",
                    "lng": 82.935566,
                    "station_id": "53.304",
                    "station_name": "Маршала Покрышкина",
                },
                "metro_stations": [
                    {
                        "lat": 55.043634,
                        "line_id": "53",
                        "line_name": "Дзержинская",
                        "lng": 82.935566,
                        "station_id": "53.304",
                        "station_name": "Маршала Покрышкина",
                    }
                ],
                "raw": "Новосибирск, улица Ломоносова, 53/1",
                "street": "улица Ломоносова",
            },
            "adv_context": None,
            "adv_response_url": None,
            "alternate_url": "https://hh.ru/vacancy/121489042",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=121489042",
            "archived": False,
            "area": {"id": "4", "name": "Новосибирск", "url": "https://api.hh.ru/areas/4"},
            "branding": {"tariff": None, "type": "MAKEUP"},
            "contacts": None,
            "created_at": "2025-06-09T18:15:13+0300",
            "department": None,
            "employer": {
                "accredited_it_employer": False,
                "alternate_url": "https://hh.ru/employer/706928",
                "employer_rating": None,
                "id": "706928",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/7178152.png",
                    "90": "https://img.hhcdn.ru/employer-logo/7178151.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1389591.png",
                },
                "name": "НЛ Континент",
                "trusted": True,
                "url": "https://api.hh.ru/employers/706928",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=706928",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "fly_in_fly_out_duration": [],
            "has_test": False,
            "id": "121489042",
            "insider_interview": None,
            "internship": False,
            "is_adv_vacancy": False,
            "name": "Backend-разработчик",
            "night_shifts": False,
            "premium": False,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "published_at": "2025-06-09T18:15:13+0300",
            "relations": [],
            "response_letter_required": False,
            "response_url": None,
            "salary": None,
            "salary_range": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_contacts": True,
            "show_logo_in_search": True,
            "snippet": {
                "requirement": "MySQL- понимать зачем нужны индексы и "
                "транзакции. Django - опыт работы от 2-х лет. "
                "Опыт работы Django Rest Framework. ",
                "responsibility": "Разработка и поддержка backend-части "
                "внутренних систем компании на "
                "<highlighttext>Python</highlighttext> 2.7 и "
                "<highlighttext>Python</highlighttext> 3.9. "
                "Модернизация, оптимизация и "
                "масштабирование...",
            },
            "sort_point_distance": None,
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/121489042?host=hh.ru",
            "work_format": [{"id": "ON_SITE", "name": "На\xa0месте работодателя"}],
            "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
            "working_days": [],
            "working_hours": [{"id": "HOURS_8", "name": "8\xa0часов"}],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": False,
            "accept_temporary": False,
            "address": {
                "building": "42",
                "city": "Москва",
                "description": None,
                "id": "7101916",
                "lat": 55.783681,
                "lng": 37.630517,
                "metro": {
                    "lat": 55.779584,
                    "line_id": "5",
                    "line_name": "Кольцевая",
                    "lng": 37.633646,
                    "station_id": "5.119",
                    "station_name": "Проспект Мира",
                },
                "metro_stations": [
                    {
                        "lat": 55.779584,
                        "line_id": "5",
                        "line_name": "Кольцевая",
                        "lng": 37.633646,
                        "station_id": "5.119",
                        "station_name": "Проспект Мира",
                    }
                ],
                "raw": "Москва, улица Щепкина, 42",
                "street": "улица Щепкина",
            },
            "adv_context": None,
            "adv_response_url": None,
            "alternate_url": "https://hh.ru/vacancy/122160167",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=122160167",
            "archived": False,
            "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
            "contacts": None,
            "created_at": "2025-07-02T10:06:13+0300",
            "department": None,
            "employer": {
                "accredited_it_employer": True,
                "alternate_url": "https://hh.ru/employer/4808331",
                "employer_rating": None,
                "id": "4808331",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/4204937.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/4204936.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/941099.jpg",
                },
                "name": "РК-ЦИФРА",
                "trusted": True,
                "url": "https://api.hh.ru/employers/4808331",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=4808331",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "fly_in_fly_out_duration": [],
            "has_test": False,
            "id": "122160167",
            "insider_interview": None,
            "internship": False,
            "is_adv_vacancy": False,
            "name": "Старший системный инженер",
            "night_shifts": False,
            "premium": False,
            "professional_roles": [{"id": "114", "name": "Системный инженер"}],
            "published_at": "2025-07-02T10:06:13+0300",
            "relations": [],
            "response_letter_required": False,
            "response_url": None,
            "salary": None,
            "salary_range": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_contacts": False,
            "show_logo_in_search": None,
            "snippet": {
                "requirement": "Базовые знания принципа работы сетей: "
                "коммутация, маршрутизация, NAT. Уверенное "
                "владение <highlighttext>Python</highlighttext>, "
                "PowerShell. Опыт администрирования Zabbix: "
                "умение добавлять собственные метрики, "
                "конфигурация...",
                "responsibility": "Разработка скриптов мониторинга с помощью "
                "<highlighttext>Python</highlighttext>, "
                "PowerShell. Разработка автотестов с помощью "
                "Selenium. Автоматизировать рутинные задачи с "
                "помощью "
                "<highlighttext>Python</highlighttext>, "
                "PowerShell. ",
            },
            "sort_point_distance": None,
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/122160167?host=hh.ru",
            "work_format": [],
            "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
            "working_days": [],
            "working_hours": [{"id": "HOURS_8", "name": "8\xa0часов"}],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
    ]


@pytest.fixture
def all_vacancies() -> list[tuple]:
    return [
        (
            "1000 и одна туфелька",
            'Продавец-кассир/Продавец-консультант (ТРК "Авеню")',
            55000.0,
            None,
            "https://api.hh.ru/vacancies/120962649?host=hh.ru",
        ),
        (
            "0.75 GROUP",
            "Официант в 0.75 please Moscow",
            150000.0,
            None,
            "https://api.hh.ru/vacancies/122789405?host=hh.ru",
        ),
        (
            "0.75 GROUP",
            "Бренд-менеджер в сеть ресторанов «0.75 Group»",
            70000.0,
            90000.0,
            "https://api.hh.ru/vacancies/121654815?host=hh.ru",
        ),
        (
            "0.75 GROUP",
            "Управляющий в сеть ресторанов 0.75 GROUP",
            150000.0,
            None,
            "https://api.hh.ru/vacancies/123078303?host=hh.ru",
        ),
        ("1001pled.ru", "Менеджер по логистике", 70000.0, 80000.0, "https://api.hh.ru/vacancies/123198998?host=hh.ru"),
        ("0.75 GROUP", "Личный ассистент", 80000.0, None, "https://api.hh.ru/vacancies/121860249?host=hh.ru"),
        ("0.75 GROUP", 'Менеджер в "12 СЛОЁВ"', 55000.0, None, "https://api.hh.ru/vacancies/122811842?host=hh.ru"),
        (
            "0.75 GROUP",
            'Хостес в ресторан "0,75 please"',
            38000.0,
            None,
            "https://api.hh.ru/vacancies/123075766?host=hh.ru",
        ),
        ("1001 Крепеж", "Кладовщик", 92000.0, 103000.0, "https://api.hh.ru/vacancies/123190002?host=hh.ru"),
        (
            "0.75 GROUP",
            "Повар в сеть ресторанов 075 GROUP",
            64000.0,
            None,
            "https://api.hh.ru/vacancies/117454794?host=hh.ru",
        ),
        (
            "1000 и одна туфелька",
            "Продавец-кассир/продавец-консультант (ТРК Радуга)",
            60000.0,
            None,
            "https://api.hh.ru/vacancies/118297452?host=hh.ru",
        ),
        ("1001 чай", "Продавец-консультант", 50000.0, None, "https://api.hh.ru/vacancies/123225259?host=hh.ru"),
        ("1001 Тур", "Офис-менеджер (секретарь)", None, None, "https://api.hh.ru/vacancies/122344625?host=hh.ru"),
        (
            "1001 Тур",
            "Менеджер по туризму (м. Новогиреево)",
            200000.0,
            None,
            "https://api.hh.ru/vacancies/122783690?host=hh.ru",
        ),
        (
            "1000 ДЛЯ УДОБНОЙ ЖИЗНИ",
            "Продавец-кассир",
            40000.0,
            None,
            "https://api.hh.ru/vacancies/122175686?host=hh.ru",
        ),
        (
            "1001 LABS",
            "Инспектор по кадрам / Специалист по документообороту",
            None,
            65000.0,
            "https://api.hh.ru/vacancies/122595198?host=hh.ru",
        ),
        (
            "0704",
            "Продавец-консультант в мультибрендовое пространство женской одежды 0704",
            38000.0,
            57000.0,
            "https://api.hh.ru/vacancies/123050979?host=hh.ru",
        ),
        (
            "0not1",
            'Продавец-консультант (Универмаг "Цветной")',
            110000.0,
            None,
            "https://api.hh.ru/vacancies/122629547?host=hh.ru",
        ),
        ("1000 Ибу", "Повар горячего цеха", 90000.0, 100000.0, "https://api.hh.ru/vacancies/123273062?host=hh.ru"),
        ("1000 Свай", "Менеджер по продажам", 100000.0, None, "https://api.hh.ru/vacancies/122278607?host=hh.ru"),
        ("0.75 GROUP", "Кондитер в сеть 075 GROUP", 64000.0, None, "https://api.hh.ru/vacancies/123273683?host=hh.ru"),
        (
            "001KZ (001КЗ)",
            "Менеджер в отдел закупок / Оператор базы 1с",
            260000.0,
            None,
            "https://api.hh.ru/vacancies/123182238?host=hh.ru",
        ),
        (
            "0.75 GROUP",
            'Официант в ресторан "0,75 Please"',
            70000.0,
            None,
            "https://api.hh.ru/vacancies/122522380?host=hh.ru",
        ),
        ("0.75 GROUP", "Официант в сеть 075 GROUP", 65000.0, None, "https://api.hh.ru/vacancies/122175382?host=hh.ru"),
        ("1001 Крепеж", "Водитель-экспедитор", 80000.0, 100000.0, "https://api.hh.ru/vacancies/122747596?host=hh.ru"),
        (
            "1001pled.ru",
            "Менеджер по закупкам и снабжению",
            80000.0,
            120000.0,
            "https://api.hh.ru/vacancies/122316750?host=hh.ru",
        ),
        ("0sprava", "Менеджер по продажам", 150000.0, 500000.0, "https://api.hh.ru/vacancies/123204845?host=hh.ru"),
        (
            "0.75 GROUP",
            "Бармен в сеть ресторанов 075 GROUP",
            55000.0,
            None,
            "https://api.hh.ru/vacancies/121039230?host=hh.ru",
        ),
        ("0.75 GROUP", 'Бариста в "12 слоёв"', 40000.0, None, "https://api.hh.ru/vacancies/122470718?host=hh.ru"),
        (
            "1001 Тур (ООО Оникс)",
            "Менеджер по туризму в офисы продаж",
            25000.0,
            250000.0,
            "https://api.hh.ru/vacancies/122836972?host=hh.ru",
        ),
        ("1001 Крепеж", "Уборщица/уборщик", 45000.0, 45000.0, "https://api.hh.ru/vacancies/122416182?host=hh.ru"),
        ("1001 LABS", "Cистемный аналитик (Senior)", None, None, "https://api.hh.ru/vacancies/122902506?host=hh.ru"),
        (
            "1001pled.ru",
            "Менеджер по продажам B2B и B2G без поиска",
            110000.0,
            250000.0,
            "https://api.hh.ru/vacancies/121516429?host=hh.ru",
        ),
        (
            "1000 ДЛЯ УДОБНОЙ ЖИЗНИ",
            "Бухгалтер на первичную документацию",
            55000.0,
            None,
            "https://api.hh.ru/vacancies/122236435?host=hh.ru",
        ),
        (
            "1001 Тур",
            "Менеджер по туризму (м. Маяковская)",
            150000.0,
            None,
            "https://api.hh.ru/vacancies/122757911?host=hh.ru",
        ),
        (
            "1000 ДЛЯ УДОБНОЙ ЖИЗНИ",
            "Продавец-кассир",
            40000.0,
            None,
            "https://api.hh.ru/vacancies/121203575?host=hh.ru",
        ),
        ("0.75 GROUP", 'Пекарь в "12 слоёв"', 55000.0, None, "https://api.hh.ru/vacancies/119903597?host=hh.ru"),
        ("0250", "Главный бухгалтер", 90000.0, None, "https://api.hh.ru/vacancies/122757137?host=hh.ru"),
        (
            "001KZ (001КЗ)",
            "Оператор call-центра / менеджер по обработке заказов",
            220000.0,
            260000.0,
            "https://api.hh.ru/vacancies/122262704?host=hh.ru",
        ),
        (
            "1000 и одна туфелька",
            'Продавец-кассир/продавец-консультант (ТЦ "Меркурий")',
            55000.0,
            None,
            "https://api.hh.ru/vacancies/119397404?host=hh.ru",
        ),
        (
            "0901",
            "Продавец-консультант в магазин вина (кавист в винотеку 0901wine)",
            30000.0,
            150000.0,
            "https://api.hh.ru/vacancies/122545837?host=hh.ru",
        ),
        (
            "0.75 GROUP",
            'Сборщик в доставку "Mike&Molly" (центр)',
            45000.0,
            None,
            "https://api.hh.ru/vacancies/119741993?host=hh.ru",
        ),
        (
            "1000 ДЛЯ УДОБНОЙ ЖИЗНИ",
            "Кладовщик-комплектовщик",
            50000.0,
            None,
            "https://api.hh.ru/vacancies/122195200?host=hh.ru",
        ),
        (
            "1000 и одна туфелька",
            "Продавец-кассир/продавец-консультант ТРК Родео Драйв",
            60000.0,
            None,
            "https://api.hh.ru/vacancies/119966818?host=hh.ru",
        ),
        (
            "0.75 GROUP",
            "Сборщик на доставку «Sushi, please»",
            40000.0,
            None,
            "https://api.hh.ru/vacancies/122175375?host=hh.ru",
        ),
        (
            "0.75 GROUP",
            "Водитель-экспедитор в сеть ресторанов 075 GROUP",
            50000.0,
            50000.0,
            "https://api.hh.ru/vacancies/121620823?host=hh.ru",
        ),
        (
            "0.75 GROUP",
            "Расчетчик в сеть ресторанов",
            60000.0,
            None,
            "https://api.hh.ru/vacancies/122535389?host=hh.ru",
        ),
        ("1001 LABS", "Инженер технической поддержки", None, None, "https://api.hh.ru/vacancies/122201566?host=hh.ru"),
        (
            "1000 ДЛЯ УДОБНОЙ ЖИЗНИ",
            "Уборщик производственных помещений",
            12000.0,
            12400.0,
            "https://api.hh.ru/vacancies/122233264?host=hh.ru",
        ),
        (
            "0.75 GROUP",
            "Су-шеф в сеть ресторанов 075 GROUP",
            72000.0,
            None,
            "https://api.hh.ru/vacancies/121848018?host=hh.ru",
        ),
        (
            "001KZ (001КЗ)",
            "Специалист по претензиям и возвратам поставщикам",
            None,
            320000.0,
            "https://api.hh.ru/vacancies/122633943?host=hh.ru",
        ),
        (
            "1001 Тур",
            "Менеджер по туризму (м. Отрадное)",
            150000.0,
            None,
            "https://api.hh.ru/vacancies/121696680?host=hh.ru",
        ),
        ("0250", "Менеджер по продажам", 50000.0, 80000.0, "https://api.hh.ru/vacancies/122754891?host=hh.ru"),
        (
            "1000 и одна туфелька",
            "Продавец в магазин детской обуви (Green Park)",
            50000.0,
            None,
            "https://api.hh.ru/vacancies/120424257?host=hh.ru",
        ),
        (
            "0.75 GROUP",
            "Главный бухгалтер в ресторан",
            110000.0,
            150000.0,
            "https://api.hh.ru/vacancies/122765781?host=hh.ru",
        ),
        (
            "1001 LABS",
            "Руководитель проекта / внедрения ИТ-продуктов",
            None,
            None,
            "https://api.hh.ru/vacancies/122617491?host=hh.ru",
        ),
        (
            "0.75 GROUP",
            "Бухгалтер-калькулятор в сеть ресторанов 0.75 GROUP",
            None,
            55000.0,
            "https://api.hh.ru/vacancies/121428578?host=hh.ru",
        ),
        (
            "1000 ДЛЯ УДОБНОЙ ЖИЗНИ",
            "Продавец-кассир",
            40000.0,
            None,
            "https://api.hh.ru/vacancies/121256721?host=hh.ru",
        ),
        (
            "1000 ДЛЯ УДОБНОЙ ЖИЗНИ",
            "Продавец-кассир (В. Волошиной,38)",
            40000.0,
            None,
            "https://api.hh.ru/vacancies/122300595?host=hh.ru",
        ),
        (
            "1001pled.ru",
            "Механик вязальных станков",
            90000.0,
            100000.0,
            "https://api.hh.ru/vacancies/122480944?host=hh.ru",
        ),
        (
            "1000 ДЛЯ УДОБНОЙ ЖИЗНИ",
            "Продавец-кассир в ТЦ Ноград (Ленинский район)",
            40000.0,
            None,
            "https://api.hh.ru/vacancies/120364691?host=hh.ru",
        ),
        ("062 detail", "Детейлер автомойщик", 60000.0, None, "https://api.hh.ru/vacancies/122462518?host=hh.ru"),
        (
            "1001 LABS",
            "BI Team Lead/ Руководитель команды BI-аналитиков",
            None,
            None,
            "https://api.hh.ru/vacancies/122902537?host=hh.ru",
        ),
        (
            "1000 ДЛЯ УДОБНОЙ ЖИЗНИ",
            "Продавец- грузчик (ТЦ Радуга)",
            40000.0,
            None,
            "https://api.hh.ru/vacancies/123125488?host=hh.ru",
        ),
        (
            "1000 ДЛЯ УДОБНОЙ ЖИЗНИ",
            "Продавец-кассир (Ул. Металлистов, 4Б)",
            40000.0,
            None,
            "https://api.hh.ru/vacancies/120364690?host=hh.ru",
        ),
        (
            "1000 ДЛЯ УДОБНОЙ ЖИЗНИ",
            "Продавец-кассир (ТЦ Облака)",
            40000.0,
            56000.0,
            "https://api.hh.ru/vacancies/120365162?host=hh.ru",
        ),
        (
            "1000 и одна туфелька",
            'Продавец-консультант / продавец-кассир (ТЦ "Балкания Нова")',
            55000.0,
            None,
            "https://api.hh.ru/vacancies/121787040?host=hh.ru",
        ),
        (
            "1000 ДЛЯ УДОБНОЙ ЖИЗНИ",
            "Продавец-кассир (ТП Cотка)",
            40000.0,
            None,
            "https://api.hh.ru/vacancies/123032016?host=hh.ru",
        ),
        (
            "1001 Тур",
            "Менеджер по туризму (м. Тульская)",
            200000.0,
            None,
            "https://api.hh.ru/vacancies/119882638?host=hh.ru",
        ),
        (
            "1001 Тур",
            "Менеджер по туризму (м. Сокол)",
            200000.0,
            None,
            "https://api.hh.ru/vacancies/120494532?host=hh.ru",
        ),
        (
            "1001 Тур",
            "Менеджер по туризму (м. Новослободская)",
            200000.0,
            None,
            "https://api.hh.ru/vacancies/121073618?host=hh.ru",
        ),
        (
            "1000 ДЛЯ УДОБНОЙ ЖИЗНИ",
            "Продавец-кассир (ТЦ Южный Квартал)",
            40000.0,
            None,
            "https://api.hh.ru/vacancies/121652872?host=hh.ru",
        ),
    ]


@pytest.fixture
def vacancies_with_higher_salary() -> list[tuple]:
    return [
        (
            122789405,
            1823,
            "Официант в 0.75 please Moscow",
            "https://api.hh.ru/vacancies/122789405?host=hh.ru",
            150000.0,
            None,
            None,
            None,
        ),
        (
            123078303,
            1823,
            "Управляющий в сеть ресторанов 0.75 GROUP",
            "https://api.hh.ru/vacancies/123078303?host=hh.ru",
            150000.0,
            None,
            "Организацией бесперебойной работы ресторана. Организацией и контролем за "
            "соблюдением стандартов сервиса. Выполнять ключевые показатели. Работать с "
            "финансовой отчетностью по заведению. ",
            'Два года подряд мы "Лучший ресторан Сибири" и конечно не собираемся на на '
            "этом останавливаться. У вас опыт аналогичной работы...",
        ),
        (
            123190002,
            1826,
            "Кладовщик",
            "https://api.hh.ru/vacancies/123190002?host=hh.ru",
            92000.0,
            103000.0,
            "Разгрузка/погрузка товаров (ручная или с использованием "
            "погрузчиков/штабелеров). Приемка/ оприходование товара в 1С. Комплектация "
            "заказов. Складской документооборот.",
            "Знание 1С (желательно). Приветствуется опыт управления погрузчиком и знание " "строительного крепежа.",
        ),
        (
            122783690,
            1832,
            "Менеджер по туризму (м. Новогиреево)",
            "https://api.hh.ru/vacancies/122783690?host=hh.ru",
            200000.0,
            None,
            "Качественный подбор и продажа туристических услуг. Общение с клиентами в "
            "офисе и по телефону. Оформление сопроводительной документации, выдача "
            "документов. ",
            "Ваш опыт в туризме от года. Вы знаете основные туристические направления и "
            "курорты. Знаете технику продажи и умеете применять ее...",
        ),
        (
            122629547,
            1830,
            'Продавец-консультант (Универмаг "Цветной")',
            "https://api.hh.ru/vacancies/122629547?host=hh.ru",
            110000.0,
            None,
            "Консультировать клиентов, вдохновлять на покупки и рассказывать о бренде. "
            "Сопровождать к кассе (никакой рутины – только продажи и общение). ",
            "Опыт в продажах – плюс, но главное – харизма и желание зарабатывать. Любовь "
            "к streetwear и моде – будет легче.",
        ),
        (
            123273062,
            1833,
            "Повар горячего цеха",
            "https://api.hh.ru/vacancies/123273062?host=hh.ru",
            90000.0,
            100000.0,
            None,
            None,
        ),
        (
            122278607,
            1834,
            "Менеджер по продажам",
            "https://api.hh.ru/vacancies/122278607?host=hh.ru",
            100000.0,
            None,
            "Развивать продажи винтовых свай. Обрабатывать входящие заявки от клиентов. "
            "Развивать клиентскую базу, вести переговоры клиентами. Выставлять счета, "
            "оформлять договора. ",
            "Опыт работы активных продаж строительных материалов/металлопроката. Высокий "
            "уровень коммуникативных навыков. Владение MS Excel, MS Word, на уверенном "
            "уровне. ",
        ),
        (
            123182238,
            1738,
            "Менеджер в отдел закупок / Оператор базы 1с",
            "https://api.hh.ru/vacancies/123182238?host=hh.ru",
            260000.0,
            None,
            "Работа с поставщиками по оформлению заявок. Контроль проведения "
            "взаиморасчетов; контроль передачи данных в логистику. Контроль поступления "
            "товара. Контроль и оформление...",
            "Высокая оперативность обработки данных, умение работать с шириной "
            "номенклатуры. Развитые навыки коммуникаций. Знание 1С (предпочтительно "
            "Управление торговлей). ",
        ),
        (
            123204845,
            1835,
            "Менеджер по продажам",
            "https://api.hh.ru/vacancies/123204845?host=hh.ru",
            150000.0,
            500000.0,
            "Продукт: Умаг — автоматизация магазинов и ритейла. Обрабатывать входящие "
            "заявки из рекламы и сайта. Вести текущую клиентскую базу в CRM (AMO...",
            "Опыт продаж B2B / SaaS / IT-решений — будет плюсом. Грамотная речь, умение "
            "убеждать и доносить ценность. Уверенное пользование ПК...",
        ),
        (
            121516429,
            1825,
            "Менеджер по продажам B2B и B2G без поиска",
            "https://api.hh.ru/vacancies/121516429?host=hh.ru",
            110000.0,
            250000.0,
            "Звонки по действующей клиентской базе, актуализация потребностей и "
            "контактов, проработка проектов и ведение сделки. Работа в CRM и отчетность "
            "по...",
            "Грамотная устная и письменная речь, законченное высшее образование, "
            "эмоциональный интеллект, обязательно зрелый как личность, порядочность.",
        ),
        (
            122757911,
            1832,
            "Менеджер по туризму (м. Маяковская)",
            "https://api.hh.ru/vacancies/122757911?host=hh.ru",
            150000.0,
            None,
            "Качественный подбор туристических услуг и их продажа (массовые "
            "направления). Оформление сопроводительной документации, выдача документов. "
            "Личное общение с клиентами и по...",
            "Ваш опыт в туризме ОБЯЗАТЕЛЕН от 1 года (продажа туров в ТА). Вы знаете "
            "основные туристические направления, курорты. ",
        ),
        (
            122757137,
            1837,
            "Главный бухгалтер",
            "https://api.hh.ru/vacancies/122757137?host=hh.ru",
            90000.0,
            None,
            "ОСНО. - УСН без НДС. - ОСНО, нулевая отчетность. Объекты учета: - "
            "Бухгалтерский учет. - Управленческий учет. - Налоговый учет. Работав в "
            'учетных программах "1...',
            "Вид налогообложения предприятий:",
        ),
        (
            122262704,
            1738,
            "Оператор call-центра / менеджер по обработке заказов",
            "https://api.hh.ru/vacancies/122262704?host=hh.ru",
            220000.0,
            260000.0,
            "Консультация по входящим/исходящим звонкам, прием обращений от клиентов. "
            "Оформление и отслеживание заказов в базе 1С. Ведение переписки в...",
            "Грамотная речь и хорошая дикция. Уверенный пользователь ПК. Быстрая "
            "обучаемость, ответственность, усидчивость. Стрессоустойчивость и умение "
            "работать с возражениями. ",
        ),
        (
            121696680,
            1832,
            "Менеджер по туризму (м. Отрадное)",
            "https://api.hh.ru/vacancies/121696680?host=hh.ru",
            150000.0,
            None,
            "Качественный подбор туристических услуг и их продажа (массовые "
            "направления). Оформление сопроводительной документации, выдача документов. "
            "Личное общение с клиентами и по...",
            "Ваш опыт в туризме ОБЯЗАТЕЛЕН от 1 года (продажа туров в ТА). Вы знаете "
            "основные туристические направления, курорты. ",
        ),
        (
            122765781,
            1823,
            "Главный бухгалтер в ресторан",
            "https://api.hh.ru/vacancies/122765781?host=hh.ru",
            110000.0,
            150000.0,
            "Внесение всей первичной документации в программы IIKO и 1С. Оплата "
            "поставщиков. Формирование и реализация учетной политики предприятия. ",
            "Опыт работы главным бухгалтером / бухгалтером не менее 3 лет. Опыт работы в "
            "ресторанном бизнесе приветствуется. Уверенные знания налогового "
            "законодательства и...",
        ),
        (
            122480944,
            1825,
            "Механик вязальных станков",
            "https://api.hh.ru/vacancies/122480944?host=hh.ru",
            90000.0,
            100000.0,
            "Профилактическая чистка и продувка вязальных станков - 10 штук. Плановое "
            "техническое обслуживание и ремонт по необходимости. Хозяйственные работы в "
            "цеху.",
            "Обязательно(!) профильный опыт работы Shima Seiki, Cixing. Все необходимые "
            "документы. Умение налаживать контакт с коллективом, позитивный настрой.",
        ),
        (
            119882638,
            1832,
            "Менеджер по туризму (м. Тульская)",
            "https://api.hh.ru/vacancies/119882638?host=hh.ru",
            200000.0,
            None,
            "Качественный подбор и продажа туристических услуг. Общение с клиентами в "
            "офисе и по телефону. Оформление сопроводительной документации, выдача "
            "документов. ",
            "Ваш опыт в туризме от года. Вы знаете основные туристические направления и "
            "курорты. Знаете технику продажи и умеете применять ее...",
        ),
        (
            120494532,
            1832,
            "Менеджер по туризму (м. Сокол)",
            "https://api.hh.ru/vacancies/120494532?host=hh.ru",
            200000.0,
            None,
            "Качественный подбор и продажа туристических услуг. Общение с клиентами в "
            "офисе и по телефону. Оформление сопроводительной документации, выдача "
            "документов. ",
            "Ваш опыт в туризме от года. Вы знаете основные туристические направления и "
            "курорты. Знаете технику продажи и умеете применять ее...",
        ),
        (
            121073618,
            1832,
            "Менеджер по туризму (м. Новослободская)",
            "https://api.hh.ru/vacancies/121073618?host=hh.ru",
            200000.0,
            None,
            "Качественный подбор и продажа туристических услуг. Общение с клиентами в "
            "офисе и по телефону. Оформление сопроводительной документации, выдача "
            "документов. ",
            "Ваш опыт в туризме от года. Вы знаете основные туристические направления и "
            "курорты. Знаете технику продажи и умеете применять ее...",
        ),
    ]


[
    (
        122789405,
        1823,
        "Официант в 0.75 please Moscow",
        "https://api.hh.ru/vacancies/122789405?host=hh.ru",
        150000.0,
        None,
        None,
        None,
    ),
    (
        122522380,
        1823,
        'Официант в ресторан "0,75 Please"',
        "https://api.hh.ru/vacancies/122522380?host=hh.ru",
        70000.0,
        None,
        "Подготовка зала к приему посетителей (уборка, сервировка). Встреча и "
        "обслуживание гостей согласно стандартам работы ресторана. Соблюдение "
        "порядка и санитарных норм...",
        "Опыт работы в общепите от полугода. Отличные коммуникативные навыки. Умение "
        "работать в команде. Активность и желание развиваться в сфере гастрономии.",
    ),
    (
        122175382,
        1823,
        "Официант в сеть 075 GROUP",
        "https://api.hh.ru/vacancies/122175382?host=hh.ru",
        65000.0,
        None,
        "Обслуживать гостей на высшем уровне. Изучать меню и вина. Предлагать "
        "рекомендаций по блюдам и напиткам. Участвовать в поддержании атмосферы "
        "ресторана. ",
        "Готовы рассмотреть как с опытом, так и без. Отличные коммуникативные "
        "навыки. Умение работать в команде. Активность и желание развиваться в...",
    ),
]
