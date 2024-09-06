from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "contact"

urlpatterns = [
   path('dashboard/',views.dashboard,name="dashboard"),
   path('addcontact/',views.addcontact,name= "addcontact"),
   path('update/<int:id>',views.updatecontact,name = "update"),
   path('delete/<int:id>',views.deletecontact,name = "delete"),
   
  
   





]