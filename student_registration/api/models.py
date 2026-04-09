from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50, unique=True)
    section = models.CharField(max_length=50)

    def __str__(self):
        return self.name
