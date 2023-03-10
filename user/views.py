from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.tokens import RefreshToken


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]
    
    
    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                return Response(status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    
    
# class BlackListTokenView(APIView):
#     permission_classes = [AllowAny]
    
#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)