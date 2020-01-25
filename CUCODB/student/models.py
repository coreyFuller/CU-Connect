from django.db import models

# Create your models here.

class Student (models.Model):
    student = models.ForeignKey('self', on_delete=models.CASCADE)
    major = models.TextField()
    student_id = models.PositiveIntegerField()
    name = models.TextField()
    email = models.TextField()

    
class Class (models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=15)

class Hobbies (models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    hobby_name = models.CharField(max_length=128)