"""ML_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Regression.views import Regression
from Classification.views import Classification
from Clustering.views import Clustering
from Salary.views import Salary

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rank/',Regression.as_view()),
    path('car/',Classification.as_view()),
    path('profit/',Clustering.as_view()),
    path('salary/',Salary.as_view())


]
