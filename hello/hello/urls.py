"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
from django.conf import settings

from webapp.views import IndexView_good, Good_more, Good_add, Good_change, Good_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView_good.as_view(), name='main_page'),
    path('more/<int:pk>/', Good_more.as_view(), name='see_good'),
    path('add/', Good_add.as_view(), name='add_good'),
    path('edit/<int:pk>/', Good_change.as_view(), name='change_good'),
    path('delete/<int:pk>/', Good_delete.as_view(), name='del_good'),
    path('accounts/', include('accounts.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
