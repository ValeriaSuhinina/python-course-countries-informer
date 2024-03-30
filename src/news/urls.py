from django.urls import path

from news.views import get_news

urlpatterns = [
    path("news/<str:country_code>", get_news, name="news"),
]
