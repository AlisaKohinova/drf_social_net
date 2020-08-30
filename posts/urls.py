from django.urls import path

from .views import (
    PostListView,
    PostCreateView,
    PostLikeView,
    LikeListView,
)



urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('create-post/', PostCreateView.as_view()),
    path('like-post/<int:post_id>/', PostLikeView.as_view()),
    path('likes/', LikeListView.as_view()),

]
