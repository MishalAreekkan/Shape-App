from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from .models import Avatar
from .serializers import AvatarSerializer
from rest_framework.exceptions import NotFound

# Create your views here.


class AvatarView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = AvatarSerializer

    def get_object(self):
        try:
            return Avatar.objects.get_or_create(user=self.request.user)[0]
        except Exception as e:
            raise NotFound(f"Error retrieving or creating avatar: {str(e)}")

    def get(self, request):
        try:
            instance = (
                self.get_object()
            )
            serializer = AvatarSerializer(instance) 
            return Response(serializer.data) 
        except NotFound as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(
                {"detail": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def post(self, request):
        instance = self.get_object()
        serializer = AvatarSerializer(
            instance, data=request.data, partial=True
        )

        if serializer.is_valid():
            serializer.save()  
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            ) 
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
