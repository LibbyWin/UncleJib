from django.shortcuts import render, redirect
from . import views


# Create your views here.
def about(request):
    context = {
        'about_page': 'active'
    }

    return render(request, 'pages/about.html', context)



def delivery(request):
    context = {
        'delivery_page': 'active'
    }

    return render(request, 'pages/delivery.html', context)


def faqs(request):
    context = {
        'faqs_page': 'active'
    }

    return render(request, 'pages/faqs.html', context)


def index(request):
    context = {
        'index_page': 'active'
    }

    return render(request, 'pages/index.html', context)

def returns(request):
    context = {
        'returns_page': 'active'
    }

    return render(request, 'pages/returns.html', context)

# Create your views here.
def contact(request):
    context = {
        'contact_page': 'active'
    }

    return render(request, 'pages/contact.html', context)
