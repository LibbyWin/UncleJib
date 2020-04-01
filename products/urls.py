from django.conf.urls import url, include
from .views import all_categories, product, all_products

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^all_mountain$', product, name='all_mountain'),
    url(r'^big_mountain$', product, name='big_mountain'),
    url(r'^freestyle$', product, name='freestyle'),
    url(r'^pipe_park$', product, name='pipe_park'),
    url(r'^jib_street$', product, name='jib_street'),
    url(r'^boardercross$', product, name='boardercross'),
    url(r'^(?P<slug>[\w-]+)$', product, name='product_detail'),
]