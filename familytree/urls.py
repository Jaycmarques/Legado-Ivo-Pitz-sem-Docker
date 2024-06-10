from django.urls import path
from . import views


# familytree/urls.py


urlpatterns = [
    path('', views.familytree, name='index'),
    path('detail/', views.detail, name='detail'),
]