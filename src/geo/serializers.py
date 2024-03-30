from rest_framework import serializers

from geo.models import Country, City


class CountrySerializer(serializers.ModelSerializer):
    """
    Сериализатор для данных о стране.
    """

    class Meta:
        model = Country
        fields = [
            "id",
            "name",
            "alpha2code",
            "alpha3code",
            "capital",
            "region",
            "subregion",
            "population",
            "latitude",
            "longitude",
            "demonym",
            "area",
            "numeric_code",
            "flag",
            "currencies",
            "languages",
        ]


class CitySerializer(serializers.ModelSerializer):
    """
    Сериализатор для данных о городе.
    """

    country = CountrySerializer(read_only=True)

    class Meta:
        model = City
        fields = [
            "id",
            "name",
            "region",
            "latitude",
            "longitude",
            "country",
     ]


class _coordSerializer(serializers.Serializer):
    lon = serializers.FloatField()
    lat = serializers.FloatField()

class _weatherSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    main = serializers.CharField()
    description = serializers.CharField()

class _mainSerializer(serializers.Serializer):
    temp = serializers.FloatField()
    feels_like = serializers.FloatField()
    temp_min = serializers.FloatField()
    temp_max = serializers.FloatField()
    pressure = serializers.IntegerField()
    humidity = serializers.IntegerField()


class _windSerializer(serializers.Serializer):
    speed = serializers.IntegerField()

class _cloudsSerializer(serializers.Serializer):
    all = serializers.IntegerField()

class _sysSerializer(serializers.Serializer):
    sunrise = serializers.IntegerField()
    sunset = serializers.IntegerField()

class WeatherSerializer(serializers.Serializer):
    """
    Сериализатор для данных о погоде .
    """
    coord=_coordSerializer()
    weather=serializers.ListField(child=_weatherSerializer())
    main=_mainSerializer()
    visibility = serializers.IntegerField()
    wind=_windSerializer()
    clouds=_cloudsSerializer()
    sys=_sysSerializer()
    timezone= serializers.IntegerField()
    name=serializers.CharField()
    
class CurrencySerializer(serializers.Serializer):
    """
    Сериализатор для данных о валюте.
    """
    timestamp = serializers.IntegerField()
    base = serializers.CharField()
    date = serializers.CharField()
    rates = serializers.DictField(child=serializers.FloatField())