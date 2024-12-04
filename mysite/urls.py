"""
URL configuration for LegadoIvoPitz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from pages import views as pages_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ivo-pitz', pages_views.home_view, name='home'),  # Home page
    path('safeadmin/', admin.site.urls),  # Admin do Django
    path('', include('familytree.urls')),
    path('pages/', include('pages.urls')),
]

if settings.DEBUG:
    # Import necessário para o Debug Toolbar
    import debug_toolbar
    
    # Adiciona as rotas do Debug Toolbar ao urlpatterns existente
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

    # Adiciona rotas para servir arquivos de mídia durante o desenvolvimento
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

