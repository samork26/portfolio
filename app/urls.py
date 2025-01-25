from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('about/', views.about, name='about'),
    path('experience/', views.experience, name='experience'),
    path('contact/', views.contact, name="contact")
]
