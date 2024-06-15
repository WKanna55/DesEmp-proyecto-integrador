from django.urls import path
from . import views

app_name = 'brazalete_datos'

urlpatterns = [
    path('', views.index, name="index"),
    path('closest-reminders/', views.fetch_closest_reminders, name='fetch_closest_reminders'),  # Actualizamos la ruta
]