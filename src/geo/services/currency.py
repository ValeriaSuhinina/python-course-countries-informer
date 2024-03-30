from typing import Optional

from geo.clients.currency import CurrencyClient


class CurrencyService:
    """
    Сервис для работы с данными о валюте.
    """

    def get_currency(
        self,
        base: str,
    ) -> Optional[dict]:
        """
        Получение курса валюты.
        :param country: Страна
        :return:
        """

        if data := CurrencyClient().get_rates(base):
            return data

        return None
