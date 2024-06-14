from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'brazalete_datos'

urlpatterns = [
    path('', views.index, name="index"),
     path('about/', views.about_us, name='about_us'),
    path('help/', views.help, name='help'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

