from django.urls import path

from . import views

urlpatterns = [
    path("loginx", views.loginx, name="loginx"),
    path("", views.shop, name="shop"),
    path("signup", views.signup, name="signup"),
    path("register", views.register, name="register"),
    # path("logout", views.logout, name="logout"),
]
# http://127.0.0.1:8000/cake_auth/register/
