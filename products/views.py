from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.
def all_categories(request):
    """
    shows all products under a specific category 
    ie. freestyle = feestyle snowboards
    """
    products = Product.objects.filter(choice=current_url).order_by('name')
    return render(request, "categories.html", {'products': products})

def product(request, slug):
    """
    show an individual product with all its detail
    show on the page
    """
    product = get_object_or_404(Product, slug=slug)
    product.save()
    return render(request, "product.html", {"product": product})

def all_products(request):
    """
    Show all products when /products is added onto the 
    sites url
    """
    products = Product.objects.all()
    return render(request, "categories.html", {"products": products})