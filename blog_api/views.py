from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, RetrieveDestroyAPIView
from blog.models import Post
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.parsers import MultiPartParser, FormParser



class PostWritePermission(BasePermission):
    # Custom Permission Class
    message = "Editing Post Is Restricted To The Admin Only"
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.author == request.user


class PostViewset(viewsets.ModelViewSet):
    # permission_classes = [PostWritePermission, IsAuthenticated]
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
    
    
class CreatePost(APIView):
    # permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    
    
    def post(self, request, format=None):
        Serializer = PostSerializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class AdminPostDetail(RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class EditPost(UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class DeletePost(RetrieveDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer