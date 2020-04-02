from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.


def product(request, product_id):
    """
    show an individual product with all its detail
    show on the page
    """
    product = get_object_or_404(Product, id=product_id)
    return render(request, "product.html", {"product": product})

def all_products(request):
    """
    Show all products when /products is added onto the 
    sites url
    """
    products = Product.objects.all()
    return render(request, "categories.html", {"products": products})

def category(request, cat):
    products = Product.objects.filter(choice=cat)
    return render(request, "categories.html", {"products": products})
