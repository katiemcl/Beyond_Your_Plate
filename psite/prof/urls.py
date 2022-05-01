from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('workshop/', views.workshop, name="workshop"),
    path('yourturn/', views.yourturn, name="yourturn"),
    path('contact/', views.contact, name="contact"),
]