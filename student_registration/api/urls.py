from django.urls import path
from .views import StudentListCreateView, StudentDetailView, LoginView

urlpatterns = [
    path('students/', StudentListCreateView.as_view()),
    path('students/<int:pk>/', StudentDetailView.as_view()),
    path('login/', LoginView.as_view()),
]