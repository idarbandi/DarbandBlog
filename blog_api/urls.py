from django.urls import path
from .views import PostViewset, PostSearchView
from rest_framework.routers import DefaultRouter

Router = DefaultRouter()
Router.register("", PostViewset, basename="post")


urlpatterns = [
    path('search/', PostSearchView.as_view(), name="search"),
    ] + Router.urls