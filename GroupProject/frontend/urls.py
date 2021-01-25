from django.urls import path
from .views import index, create, welcome, login
urlpatterns = [
    path('welcome', index, name='index'),
    path('', welcome),
    path('login', login, name="login")

]
