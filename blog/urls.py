from django.urls import path
from .views import blog_list, blog_detail, blog_create

urlpatterns = [
    path('blogs/', blog_list, name='blog_list'),
    path('blogs/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('blogs/new/', blog_create, name='blog_create'),
]
