from django.shortcuts import render, get_object_or_404
from .models import Product
from reviews.models import Review


# Create your views here.


def product(request, product_id):
    """
    show an individual product with all its detail
    show on the page
    """
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST' and request.user.is_authenticated and request.POST['content'].strip() != '':
        Review.objects.create(product=product, user=request.user, content=request.POST['content'])

    reviews = Review.objects.filter(product=product)
    return render(request, "product.html", {"product": product, 'reviews': reviews})

def all_products(request):
    """
    Show all products when /products is added onto the 
    sites url
    """
    products = Product.objects.all()
    return render(request, "categories.html", {"products": products})

def category(request, cat):
    """
    will render the products inside a category
    """
    products = Product.objects.filter(choice=cat)
    return render(request, "categories.html", {"products": products})
