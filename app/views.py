from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def experience(request):
    return render(request, 'experience.html')

def contact(request):
    return render(request, 'contact.html')
