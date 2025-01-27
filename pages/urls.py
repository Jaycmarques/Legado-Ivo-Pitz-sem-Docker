from django.urls import path
from pages import views

app_name = 'pages'
urlpatterns = [
    path('criar-dedicatoria', views.criar_dedicatoria, name='criar-dedicatoria'),
    path('dedicatorias', views.dedicatorias_view, name='dedicatorias'),
    path('<slug:slug>', views.detalhe, name='detalhe'),
    # path("__debug__/", include("debug_toolbar.urls")),
]
