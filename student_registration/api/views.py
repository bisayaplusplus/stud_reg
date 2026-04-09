from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from .serializers import LoginSerializer

from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



# LIST + CREATE
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# RETRIEVE + UPDATE + DELETE
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# LOGIN

from rest_framework import generics

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user:
                return Response({"message": "Login successful"})
            return Response({"error": "Invalid credentials"}, status=401)

        return Response(serializer.errors, status=400)