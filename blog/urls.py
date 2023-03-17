from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreate.as_view(), name='user_list_create'),
    path('users/<int:pk>', views.UserRetrieveUpdateDestroy.as_view(), name='user_retrieve_update_destroy'),
    path('users/delete_all', views.UserDeleteAll.as_view(), name='user_delete_all'),
    path('posts/', views.PostListCreate.as_view(), name='post_list_create'),
    path('posts/<int:pk>', views.PostRetrieveUpdateDestroy.as_view(), name='post_retrieve_update_destroy'),
    path('posts/delete_all', views.PostDeleteAll.as_view(), name='post_delete_all'),
    path('comments/', views.CommentListCreate.as_view(), name='comment_list_create'),
    path('comments/<int:pk>', views.CommentRetrieveUpdateDestroy.as_view(), name='comment_retrieve_update_destroy'),
    path('comments/delete_all', views.CommentDeleteAll.as_view(), name='comment_delete_all'),
]