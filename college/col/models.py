from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Name: {self.name} | Subject: {self.subject}'
    
class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(default=18)
    phone=models.IntegerField(default=0)

    def __str__(self):
        return f'Student name:{self.first_name} Course:{self.course}'