"""greenhouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include

# Importamos 'DefaultRouter' de Django REST Framework y la vista 'jugos' 
from rest_framework.routers import DefaultRouter
from housefts import views as house_views
 
router = DefaultRouter()
router.register(r'getEnviroment', house_views.EnviromentViewSet, basename='house')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('housefts/',include('housefts.urls')),
    path('', include(router.urls)),
    path('house/crear', house_views.SaveEnviroment.as_view(template_name = "house/crear.html"), name='crear'),
]
