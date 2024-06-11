from django.urls import path
from . import views

app_name = 'brazalete_datos'

urlpatterns = [
    path('', views.index, name="index"),
     path('about/', views.about_us, name='about_us'),
    path('help/', views.help, name='help'),
]

