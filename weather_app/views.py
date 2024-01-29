from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import CityInput
from .serializers import CityInputSerilalizer
from .forms import CityInputForm


@api_view(['GET'])
def get_city(request, format=None):
    """Function to return inputed cities."""
    cities = CityInput.objects.all()
    serializer = CityInputSerilalizer(cities, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_city(request):
    """Function to input new city."""
    serializer = CityInputSerilalizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


def input_form(request):
    form = CityInputForm()
    context = {"form": form}
    return render(request, 'templates/form.html', context)
