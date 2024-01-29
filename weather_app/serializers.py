from rest_framework import serializers
from weather_app.models import CityInput


class CityInputSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = CityInput
        fields = '__all__'
