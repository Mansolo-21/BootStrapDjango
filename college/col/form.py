from django import forms
from . models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        field=['firstname', 'age' ]