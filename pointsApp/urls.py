"""pointsApp URL Configuration

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
from django.urls import path, include
from pagesManager.views import *
from yogurt.views import *
from bread.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', login_view, name='login_view'),
    path('login_view/', login_view, name='login_view'),
    path('home_view/', home_view, name='home_view'),
    path('login/', login_func, name='login'),
    path('logout/', logout_func, name='logout'),
    path('change_pass/', change_pass_func, name='change_pass'),
    path('set_lang_en/', set_lang_en_func, name='set_lang_en'),
    path('set_lang_es/', set_lang_es_func, name='set_lang_es'),

    path('yogurt_view/', yogurt_view, name='yogurt_view'),
    path('yogurt_checkIn/', yogurt_checkIn, name='yogurt_checkIn'),
    path('yogurt_set_checkIn/', yogurt_set_checkIn, name='yogurt_set_checkIn'),    
    path('yogurt_cus_view/', yogurt_cus_view, name='yogurt_cus_view'),
    path('yogurt_cus_edit/<int:id>', yogurt_cus_edit, name='yogurt_cus_edit'),
    path('yogurt_checkin_mannager/', yogurt_checkin_mannager, name='yogurt_checkin_mannager'),
    #path('yogurt_checkin_edit/<int:id>', yogurt_checkin_edit, name='yogurt_checkin_edit'),
    path('yogurt_setPrice/', yogurt_setPrice, name='yogurt_setPrice'),
    path('yogurt_sent_sms/', yogurt_sent_sms, name='yogurt_sent_sms'),
    path('yogurt_order_view/', yogurt_order_view, name='yogurt_order_view'),

]
