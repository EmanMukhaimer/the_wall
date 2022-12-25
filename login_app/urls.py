from django.urls import path
from . import views
app_name = 'login'
urlpatterns = [
    path('', views.index),
    path('success', views.display_user),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
]