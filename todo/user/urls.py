from urllib.parse import urlparse
from django.urls import URLPattern, path
from user import views

urlpatterns = [
    path('register/', views.user_register, name="user_register"),
    path('login/', views.user_login, name="user_login"),
]


