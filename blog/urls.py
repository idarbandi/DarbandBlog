from django.urls import path, include
from .views import Blog

urlpatterns = [
    path("posts", Blog.as_view(), name="main" ),
]
