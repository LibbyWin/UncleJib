from django.shortcuts import render, get_object_or_404
from products.models import Category, Product


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

def index(request, category_slug=None):
    """A view that renders the index page"""
    category_page = None
    products = None
    if category_slug !=None:
        category_page = get_object_or_404(Category, slug=category_slug)
        products = Product.object.filter(category=category_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)
    
    return render(request, "index.html", {'categories': category_page, 'products': products})
