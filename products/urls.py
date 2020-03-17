from django.conf.urls import url, incluse
from .views import all_products

urlspatterns = [
    url(r'^$', all_products, name='products'),
]