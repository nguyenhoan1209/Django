from django.contrib import admin
from django.urls import path
from base import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('upload/',views.upload_file),
    path('hihi/',views.hihi),
]
