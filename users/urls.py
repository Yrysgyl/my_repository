from django.urls import path
from .views import LoginUser, LogoutUser, RegisterUser

app_name = 'users'

urlpatterns = [
    path('users/login/', LoginUser.as_view(), name='login'),
    path('users/logout/', LogoutUser.as_view(), name='logout'),
    path('users/register/', RegisterUser.as_view(), name='register'),
]