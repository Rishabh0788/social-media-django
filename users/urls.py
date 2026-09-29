from django.urls import path

from .views import (
    login_view,
    register_view,
    logout_view,
    profile_view,
    follow_user,
)


urlpatterns = [

    path(
        "",
        login_view,
        name="login",
    ),

    path(
        "login/",
        login_view,
        name="login",
    ),

    path(
        "register/",
        register_view,
        name="register",
    ),

    path(
        "logout/",
        logout_view,
        name="logout",
    ),

    path(
        "profile/<str:username>/",
        profile_view,
        name="profile",
    ),

    path(
        "profile/<str:username>/follow/",
        follow_user,
        name="follow",
    ),

]