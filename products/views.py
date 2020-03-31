from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all
    return render(request, "products.html", {"products": products})

def all_categories(request):
    product_list = Product.objects.filter(choice=current_url).order_by('name')
    return render(request, "categories.html", {'products': products})