from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #메인화면
]

