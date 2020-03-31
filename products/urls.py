from django.conf.urls import url, include
from .views import all_categories, product, all_products

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'all_mountain$', product, name='all_mountain'),
    url(r'big_mountain$', product, name='big_mountain'),
    url(r'freestyle$', product, name='freestyle'),
    url(r'pipe/park$', product, name='pipe/park'),
    url(r'jib/street$', product, name='jib/street'),
    url(r'boardercross$', product, name='boardercross'),
]