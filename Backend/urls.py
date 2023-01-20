from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog_api.urls"),name="blog"),
    path("api/user/", include("user.urls"), name="users"),
    path('api-auth/', include('rest_framework.urls'), name="rest_framework"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
