from django.urls import path
from  . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('students-life/', views.students_life, name='students_life'),
    path('news/', views.news, name='news'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('admissions/', views.admissions, name='admissions'),
    path('academics/', views.academics, name='academics'),
]