from django.urls import path
from weather_app import views

urlpatterns = [
    path('show', views.get_city, name="getData"),
    path('add', views.add_city, name="addCity"),
    path('add_form', views.input_form, name='form')
]
