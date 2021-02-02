"""task_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework_simplejwt import views as jwt_views
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/token', jwt_views.TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('login/', Login_Api.as_view(),name='login'),
    path('products_api/',Product_Api.as_view(),name="add_product"),
    path('products_list/',Product_Api.as_view(),name="list_product"),
    path('products_delete/<int:id>',Product_Api.as_view(),name="delete_product"),
    path('products_update/<int:id>/',Product_Api.as_view(),name="update_product"),
    
]
