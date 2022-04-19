from django.urls import path
from passApp import views

#TEMPLATE URLS!
app_name = 'passApp'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
