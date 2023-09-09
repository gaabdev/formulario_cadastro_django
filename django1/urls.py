"""
URL configuration for django1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from cliente.views import ClienteIndex, ClienteAdd, ClienteList, ClienteDelete, ClienteUpdate
 
urlpatterns = [
    path('', ClienteIndex.as_view(), name='client_list'),
    path('add/', ClienteAdd.as_view(), name='client_add'),
    path('list/', ClienteList.as_view(), name='client_list'),
    path('update/', ClienteUpdate.as_view(), name='client_update'),
    path('delete/', ClienteDelete.as_view(), name='client_delete'),
]
