from django.conf.urls import url, include
from .views import product, all_products, category

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^category/(?P<cat>[\w\-]+)', category, name='category'),
    #url(r'^(?P<slug>[\w-]+)$', product, name='product_detail'),
    url(r'^(?P<product_id>[0-9]+)$', product, name='product_detail'),
]