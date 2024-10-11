

from django.urls import path, include
from .views import Users, Login
urlpatterns = [
    path('registration-user/', Users.as_view(), name='save-user'),
    path('login-user/', Login.as_view(), name='login-user'),

]
