from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Name: {self.name} | Subject: {self.subject}'
    
class Student(models.Model):
    first_name=models.CharField(max_length=20)
    age=models.IntegerField
    course=models.CharField(max_length=30)
    phone=models.IntegerField
    
    def __str__(self):
        return f'Student name:{self.first_name} Course:{self.course}'