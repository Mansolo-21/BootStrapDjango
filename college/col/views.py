from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def students_life(request):
    return render(request, 'students_life.html')


def news(request):
    return render(request, 'news.html')


def events(request):
    return render(request, 'events.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to database
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    return render(request, 'contact.html')

def academics(request):
    return render(request, 'academics.html')

def admissions(request):
    return render(request, 'admissions.html')

