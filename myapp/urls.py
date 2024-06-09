from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('arvore/', views.arvore_genealogica, name='arvore_genealogica'),
]