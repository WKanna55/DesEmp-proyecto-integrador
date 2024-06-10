from django.urls import path
from . import views

app_name = 'brazalete_datos'

urlpatterns = [
    path('', views.index, name="index"),
]

