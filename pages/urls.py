from django.conf.urls import url
from .views import faqs, contact, returns, delivery, about, index

urlpatterns = [
    url(r'faqs/$', faqs, name='faqs'),    
    url(r'^contact/$', contact, name='contact'),
    url(r'delivery/$', delivery, name='delivery'),
    url(r'returns/$', returns, name='returns'),
    url(r'about/$', about, name='about'),
    url(r'index/$', index, name='index'),    
]