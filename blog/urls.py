from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('create/', views.create_blog, name='create_blog'),
    path('<int:blog_id>/edit/', views.edit_blog, name='edit_blog'),
    path('like/<int:blog_id>/', views.like_article, name='like_article'),
    path('dislike/<int:blog_id>/', views.dislike_article, name='dislike_article'),
]