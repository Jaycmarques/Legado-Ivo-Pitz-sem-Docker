from django.urls import path
from familytree import views


# familytree/urls.py

app_name = 'familytree'
urlpatterns = [
    path('', views.familytree, name='familytree_index'),
    path('detail/', views.detail, name='familytree_detail'),
    path('search/', views.search_family_member, name='search_family_member'),
]
