from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

# LIST + CREATE
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# RETRIEVE + UPDATE + DELETE
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer