from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ch1/', views.ch1, name='ch1'),
    path('ch2/', views.ch2, name='ch2'),
    path('ch3/', views.ch3, name='ch3'),
    path('ch1/calculate_ch1/', views.calculate_ch1, name='calculate_ch1'),
    path('ch2/calculate_ch2/', views.calculate_ch2, name='calculate_ch2'),
    path('ch3/calculate_ch3/', views.calculate_ch3, name='calculate_ch3'),
]
