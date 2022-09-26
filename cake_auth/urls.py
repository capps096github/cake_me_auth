from django.urls import path

from . import views

urlpatterns = [
    path("login", views.login, name="login"),
    path("", views.shop, name="shop"),
    path("signup", views.signup, name="signup"),
]
