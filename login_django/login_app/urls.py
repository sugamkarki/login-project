from django.urls import path 
from login_app import views 

app_name='login_app'

urlpatterns = [
    path('registration/', views.registration, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
