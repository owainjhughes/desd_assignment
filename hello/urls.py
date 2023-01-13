from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name='register'),
    path("booking/", views.booking, name='booking'),
]