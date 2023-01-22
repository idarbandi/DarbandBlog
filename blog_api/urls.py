from django.urls import path
from .views import PostViewset
from rest_framework.routers import DefaultRouter

Router = DefaultRouter()
Router.register("", PostViewset, basename="post")


urlpatterns = Router.urls