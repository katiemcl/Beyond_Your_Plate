from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'prof/home.html')

# Our Workshop Page
def workshop(request):
    return render(request, 'prof/workshop.html')

# Your Turn Page
def yourturn(request):
    return render(request, 'prof/yourturn.html')

# Contact pages
def contact(request):
    return render(request, 'prof/contact.html')
