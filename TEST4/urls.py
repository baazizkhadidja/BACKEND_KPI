"""TEST4 URL Configuration

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
from django.contrib import admin
from django.db import router
from django.urls import path, include
from application.api import all_inv_api, inv_detail_api, All_inv_api_filter_vset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('investissement_filter', All_inv_api_filter_vset, basename='investissement_filter')
urlpatterns = router.urls
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/investissements/', all_inv_api, name = 'all_inv_api'),
    path('api/investissement/<int:id>', inv_detail_api, name = 'inv_detail_api'),
    path('', include(router.urls))   
]