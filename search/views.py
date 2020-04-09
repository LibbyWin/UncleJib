from django.shortcuts import render
from products.models import Product

# Create your views here.
def do_search(request):
    """
    Added search bar functionalty, if there are items that are requested within the search bar it will render them.
    however, if there are no items to render, then it shall return the search template stating to either get in 
    contact or check spelling. 
    """
    products = Product.objects.filter(name__icontains=request.GET['q'])
    if products:
        return render(request, "categories.html", {"products": products})

    else:
        return render(request, "search.html")

