from django.urls import path
from .views import *


urlpatterns = [
    path('login', loginpage, name='login'),
    path('register', register, name='register'),
    path('logout', logoutpage, name='logout'),
]