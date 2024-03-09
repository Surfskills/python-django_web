from django.shortcuts import render
from .models import *
from rest_framework import status
from random import randrange
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db.models import Q
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes, action
from django.http import JsonResponse
from inmest_2024_api.utils import *
from users.serializers import AuthSerializer

# Create your views here.
from rest_framework import status  # Add this import statement

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    username = request.data.get("username")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    phone_number = request.data.get("phone_number")
    password = request.data.get("password")

    # Check if a user with the given username already exists
    if IMUser.objects.filter(username=username).exists():
        return JsonResponse({'error': 'Username is already taken.'}, status=status.HTTP_400_BAD_REQUEST)

    # If username does not exist, proceed to create a new user
    new_user = IMUser.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number
    )
    new_user.set_password(password)
    new_user.save()
    # Assuming AuthSerializer is correctly set up and imports are handled
    serializer = AuthSerializer(new_user, many=False)
    
    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)  # Add status prefix

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    # Your existing code for user_login function
    # Receive inputs and validate
    username = request.data.get("username")
    password = request.data.get("password")
    if not username or not password:
        return Response({"detail": "Kindly send me your username and password"}, status=status.HTTP_400_BAD_REQUEST)

    # Check user existence
    try:
        user = IMUser.objects.get(username=username)
    except IMUser.DoesNotExist:
        return Response({"detail": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Authenticate the user
    auth_user = authenticate(username=username, password=password)
    if auth_user:
        login(request, auth_user)  # Use auth_user for clarity
        serializer = AuthSerializer(auth_user, many=False)
        return Response({"result": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    
class ForgotPasswordAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get("username")
        if not username:
            return self.generate_400_response("Please provide username")

        try:
            user = IMUser.objects.get(username=username)
            otp_code = self.generate_unique_code()  # Use 'self' to reference the class method
            user.unique_code = otp_code
            user.save()
            return Response({"detail": "Please check your email for an OTP"}, status.HTTP_200_OK)
            
        except IMUser.DoesNotExist:
            return self.generate_400_response("User does not exist")

    def generate_unique_code(self):
        CHARSET = '0123456789'
        LENGTH = 4
        new_code = ''
        for i in range(LENGTH):
            new_code += CHARSET[randrange(0, len(CHARSET))]
        return new_code

    def generate_400_response(self, message):
        return Response({"detail": message}, status.HTTP_400_BAD_REQUEST)
        
class UserViewSet(viewsets.ModelViewSet):
  
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password', None)
        player_id = request.data.get('player_id', None)
    
        user = authenticate(email=email, password=password)
        login(request, user)

        