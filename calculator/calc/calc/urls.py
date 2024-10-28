"""
URL configuration for calc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from operations.views import AdditionView
from operations.views import SubtractionView
from operations.views import MultiplicationView
from operations.views import DivisionView
from operations.views import CubeView
from operations.views import BmiView,BmrView,WeightManagementView,EmiView,MileageView,SignupView,RegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',AdditionView.as_view()),
    path('subtract/',SubtractionView.as_view()),
    path('multiply/',MultiplicationView.as_view()),
    path('divide/',DivisionView.as_view()),
    path('cube/',CubeView.as_view()),
    path('bmi/',BmiView.as_view()),
    path('bmr/',BmrView.as_view()),
    path('weightmanagement/',WeightManagementView.as_view()),
    path('emi/',EmiView.as_view()),
    path('mileage/',MileageView.as_view()),
    path('signup/',SignupView.as_view()),
    path('register/',RegistrationView.as_view()),

]
