from django.urls import path
from .views import PostViewset, PostSearchView, CreatePost, AdminPostDetail, DeletePost, EditPost
from rest_framework.routers import DefaultRouter

Router = DefaultRouter()
Router.register("", PostViewset, basename="post")


urlpatterns = [
    path('search/', PostSearchView.as_view(), name="search"),
    #Post Admin Urls 
    path("admin/create/", CreatePost.as_view(), name="CreatePost"),
    path("admin/edit/postdetail/<int:pk>/", AdminPostDetail.as_view(), name="admindetailpost"),
    path("admin/edit/<int:pk>", EditPost.as_view(), name="EditPost"),
    path("admin/delete/<int:pk>", DeletePost.as_view(), name="DeletePost"),
    ] + Router.urls