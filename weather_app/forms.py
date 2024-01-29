from django.forms import ModelForm

from .models import CityInput


class CityInputForm(ModelForm):
    class Meta:
        model = CityInput
        fields = '__all__'
