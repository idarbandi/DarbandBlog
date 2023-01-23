from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from blog.models import Post
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework import filters



class PostWritePermission(BasePermission):
    # Custom Permission Class
    message = "Editing Post Is Restricted To The Admin Only"
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.author == request.user


class PostViewset(viewsets.ModelViewSet):
    permission_classes = [PostWritePermission]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)
    
        
        
class PostSearchView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['slug']