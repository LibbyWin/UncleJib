from django.shortcuts import render

# Create your views here.

def about(request):
    """A View that renders the about page"""
    return render(request, "about.html")

def contact(request):
    """A View that renders the contact page"""
    return render(request, "contact.html")

def delivery(request):
    """A View that renders the delivery page"""
    return render(request, "delivery.html")

def faqs(request):
    """A View that renders the faqs page"""
    return render(request, "faqs.html")

def returns(request):
    """A View that renders the returnss page"""
    return render(request, "returns.html")

def index(request):
    """A view that renders the index page"""
    return render(request,"index.html")