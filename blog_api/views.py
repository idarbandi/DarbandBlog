from rest_framework import generics
from blog.models import Post
from rest_framework.permissions import BasePermission, SAFE_METHODS
from .serializers import PostSerializer


class PostWritePermission(BasePermission):
    # Custom Permission Class
    message = "Editing Post Is Restricted To The Admin Only"
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.author == request.user
            
        
        return obj.author == request.user

class Postlist(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer 


class PostDetail(generics.RetrieveDestroyAPIView, PostWritePermission):
    queryset = Post.objects.all()
    permission_classes = [PostWritePermission]
    serializer_class = PostSerializer 