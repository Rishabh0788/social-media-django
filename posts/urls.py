from django.urls import path

from .views import (
    home,
    delete_post,
    like_post,
    add_comment
)


urlpatterns = [

    path(
        "home/",
        home,
        name="home"
    ),

    path(
        "post/<int:post_id>/delete/",
        delete_post,
        name="delete_post"
    ),

    path(
        "post/<int:post_id>/like/",
        like_post,
        name="like_post"
    ),

    path(
        "post/<int:post_id>/comment/",
        add_comment,
        name="add_comment"
    ),

]