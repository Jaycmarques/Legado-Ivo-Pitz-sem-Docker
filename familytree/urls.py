from django.urls import path
from django.contrib.auth import views as auth_views
from familytree import views


# familytree/urls.py

app_name = 'familytree'
urlpatterns = [
    path('', views.familytree, name='familytree_index'),
    path('member/<int:member_id>/', views.detail, name='familytree_detail'),
    path('search/', views.search_family_member, name='search_family_member'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
