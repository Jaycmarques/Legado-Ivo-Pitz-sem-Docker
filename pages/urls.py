from django.urls import path
from pages import views

app_name = 'pages'
urlpatterns = [
    path('dedicatoria-criar', views.criar_dedicatoria, name='dedicatoria-criar'),
    path('dedicatorias/<int:id>/', views.dedicatoria_detalhes, name='dedicatoria-detalhes'),
    path('dedicatorias', views.dedicatorias_view, name='dedicatorias'),
    path('<slug:slug>', views.detalhe, name='detalhe'),
    # path("__debug__/", include("debug_toolbar.urls")),
]
