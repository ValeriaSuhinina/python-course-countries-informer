"""
Функции для взаимодействия с внешним сервисом-провайдером данных о погоде.
"""
from http import HTTPStatus
from typing import Optional

import httpx

from app.settings import REQUESTS_TIMEOUT, API_KEY_APILAYER
from base.clients.base import BaseClient


class CurrencyClient(BaseClient):
    """
    Реализация функций для взаимодействия с внешним сервисом-провайдером данных о валюте.
    """

    def get_base_url(self) -> str:
        return "https://api.apilayer.com/fixer/latest"

    def _request(self, endpoint: str) -> Optional[dict]:
        with httpx.Client(timeout=REQUESTS_TIMEOUT) as client:
            headers = {"apikey": API_KEY_APILAYER}
            # получение ответа
            response = client.get(endpoint, headers=headers)
            if response.status_code == HTTPStatus.OK:
                return response.json()

            return None


    def get_rates(self, base: str = "rub") -> Optional[dict]:
        """
         Получение данных о курсах валют.
        :param base: Базовая валюта
        :return:
        """

        return self._request(f"{self.get_base_url()}?base={base}")


