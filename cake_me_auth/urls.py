"""cakes_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from cake_auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cake_auth/', include('cake_auth.urls')),
    path('', RedirectView.as_view(url='cake_auth/')),
    path('accounts/', include('django.contrib.auth.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
