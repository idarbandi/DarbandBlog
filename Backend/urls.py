from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.urls import path

schema_view = get_schema_view(title="Example API")

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("admin/", admin.site.urls),
    path("api/", include("blog_api.urls"),name="blog"),
    path("api/user/", include("user.urls"), name="users"),
    path('api-auth/', include('rest_framework.urls'), name="rest_framework"),
    # Documantation For Blog (coreapi)
    path("docs/", include_docs_urls(title="DarbandBlog")),
    path("schema", get_schema_view(
        title="DarbandBlog",
        description="API For All Of Your Needs",
        version="1.0.0",
    ),
         name="openAPI-Schemas")
]
