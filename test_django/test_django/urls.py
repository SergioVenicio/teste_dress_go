"""test_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.contrib.auth import views as auth_views
from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from core import views

router = routers.DefaultRouter()
router.register('produtos', views.ProdutoViewSet)

app_name = 'core'
urlpatterns = [
        path(
            'api/v1/',
            include(router.urls)
        ),
        path('', views.home, name='home'),
        path('produto/<int:id>/', views.produto, name='produto'),
        path('alugueis/', views.alugueis, name='alugueis'),
        path('aluguel/<int:id>/', views.edit_aluguel, name='edit_aluguel'),
        path(
            'login', auth_views.login,
            {'template_name': 'core/login.html'},
            name='login'
        ),
        path('user/add', views.user_add, name='user_add'),
        path(
            'logout', auth_views.logout,
            {'next_page': '/'},
            name='logout'),
        path('admin/', admin.site.urls)
]
