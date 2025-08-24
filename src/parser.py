from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями."""

    @abstractmethod
    def _connect_to_api(self) -> bool:
        """
        Абстрактный метод для подключения к API.
        """
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    Наследуется от абстрактного класса Parser.
    """

    __vacancies: list[dict]

    def __init__(self) -> None:
        """
        Инициализация класса.
        Устанавливает приватные атрибуты для URL, заголовков, параметров и списка вакансий.
        """
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params: dict = {"text": "", "page": 0, "per_page": 100, "employer_id": None}
        self.__vacancies = []

    def _connect_to_api(self) -> bool:
        """
        Приватный метод для подключения к API hh.ru.
        Отправляет запрос на базовый URL и проверяет статус-код ответа.
        """
        try:
            response = requests.get(self.__url, headers=self.__headers)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to API: {e}")
            return False

    def load_vacancies(self, companies: list[dict]) -> list[dict]:
        """Метод для получения вакансий."""

        if not self._connect_to_api():
            return []

        self.__vacancies = []  # Clear previous vacancies
        employers = []

        try:
            for company in companies:
                employers.append(company["id"])

            self.__params["employer_id"] = employers
            self.__params["page"] = 0
            while self.__params.get("page") < 20:
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                response.raise_for_status()
                data = response.json()
                if "items" in data:
                    self.__vacancies.extend(data["items"])
                else:
                    print("Warning: No 'items' key found")
                    break
                self.__params["page"] += 1
            return self.__vacancies

        except requests.exceptions.RequestException as e:
            print(f"Error loading vacancies: {e}")
            return []


class HHEmployers(Parser):
    def __init__(self) -> None:
        """
        Инициализация класса.
        Устанавливает приватные атрибуты для URL, заголовков, параметров и списка вакансий.
        """
        self.__url = "https://api.hh.ru/employers"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params: dict = {
            "text": "",
            "page": 0,
            "per_page": 10,
            "order_by": "vacancies",
            "only_with_vacancies": True,
        }
        self.__employers: list[dict] = []

    def _connect_to_api(self) -> bool:
        """
        Приватный метод для подключения к API hh.ru.
        Отправляет запрос на базовый URL и проверяет статус-код ответа.
        """
        try:
            response = requests.get(self.__url, headers=self.__headers)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to API: {e}")
            return False

    def load_employers(self) -> list[dict]:
        """Метод для получения работодателей."""

        if not self._connect_to_api():
            return []
        self.__employers = []  # Clear previous vacancies
        try:
            while self.__params.get("page") < 2:
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                response.raise_for_status()
                data = response.json()
                if "items" in data:
                    self.__employers.extend(data["items"])
                else:
                    print("Warning: No 'items' key found")
                    break
                self.__params["page"] += 1
            return self.__employers

        except requests.exceptions.RequestException as e:
            print(f"Error loading vacancies: {e}")
            return []
