from django.conf.urls import url, include
from .views import all_products, all_categories

urlpatterns = [
    url(r'^$', all_products, name='product'),
    url(r'categories/$', all_categories, name='categories'),
]