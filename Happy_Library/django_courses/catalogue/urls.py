"""django_courses URL Configuration

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

from django.urls import path
from catalogue import views
import json

urlpatterns = [
    path('', views.index, name = 'index'),
    path('available', views.free, name = 'free'),
    path('on-hold', views.on_hold, name = 'on_hold'),
    path('terms', views.terms_output, name = 'terms_output'),
]

