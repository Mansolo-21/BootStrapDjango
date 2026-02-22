from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def index(request):
    return render(request, 'col/index.html')

def about(request):
    return render(request, 'col/about.html')

def students_life(request):
    return render(request, 'col/students_life.html')

def news(request):
    return render(request, 'col/news.html')

def events(request):
    return render(request, 'col/events.html')

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

    return render(request, 'col/contact.html')

def academics(request):
    return render(request, 'col/academics.html')

def admissions(request):
    return render(request, 'col/admissions.html')

def faculty(request):
    return render(request, 'col/faculty-staff.html')

def campus(request):
    return render(request, 'col/campus-facilities.html')

def alumni(request):
    return render(request, 'col/alumni.html')

def eventd(request):
    return render(request, 'col/event-details.html')

def privacy(request):
    return render(request, 'col/privacy.html')

def terms(request):
    return render(request, 'col/terms-of-service.html')

def newsd(request):
    return render(request, 'col/news-details.html')

def error(request):
    return render(request, 'col/404.html')














