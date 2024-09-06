
from django.contrib import admin
from django.urls import path,include


from phonebook import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name= "index"),
    path('about/',views.about,name="about"),
    path('contact/',include("phonebook.urls")),
    path('user/',include("user.urls")),

    
]
