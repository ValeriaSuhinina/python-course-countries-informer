"""Представления Django"""
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from news.serializers import NewsSerializer

from news.services.news import NewsService


@api_view(["GET"])
def get_news(request: Request, country_code: str) -> JsonResponse:
    """
    Получение информации о новостях страны.
    :param Request request: Объект запроса
    :param str country_code: ISO Alpha2 код страны
    :return:
    """

    if news := NewsService().get_news(country_code):
        serializer = NewsSerializer(news, many=True)
        return JsonResponse(serializer.data, safe=False)

    raise JsonResponse([], safe=False)
