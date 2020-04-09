from django.conf.urls import url
from .views import faqs, contact, returns, delivery, about, index, covid

urlpatterns = [
    url(r'faqs/$', faqs, name='faqs'),    
    url(r'contact/$', contact, name='contact'),
    url(r'delivery/$', delivery, name='delivery'),
    url(r'returns/$', returns, name='returns'),
    url(r'about/$', about, name='about'),
    url(r'<slug:category_slug>/$', index, name='products_by_category'),
    url(r'covid/$', covid, name='covid'),
]