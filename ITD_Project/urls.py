
from django.contrib import admin
from django.urls import path
from ITD_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home)
]

