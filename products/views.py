from django.shortcuts import render
from .models import Category, Product

# Create your views here.
def all_products(request):
    products = Product.objects.all
    return render(request, "products.html", {"products": products})

def all_categories(request):
    categories = Category.objects.all
    return render(request, "categories.html", {"categories": categories})