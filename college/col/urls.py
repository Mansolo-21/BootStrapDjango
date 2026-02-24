from django.urls import path
from  . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('admissions/', views.admissions, name='admissions'),
    path('academics/', views.academics, name='academics'),
    path('faculty/', views.faculty, name='faculty'),
    path('campus/', views.campus, name='campus'),
    path('students_life/', views.students_life, name='students_life'),
    path('news/', views.news, name='news'),
    path('events/', views.events, name='events'),
    path('alumni/', views.alumni, name='alumni'),
    path('error/', views.error, name='error'),
    path('newsd/', views.newsd, name='newsd'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('event-details/', views.eventd, name='eventd'),
    path('contact/', views.contact, name='contact'),
    path('virtual-tour/', views.virtual_tour, name='virtual-tour'),
]