from django.conf.urls import url, include
from . import urls_reset
from .views import index, register, profile, logout, login

urlpatterns = [
    #take you to register page
    url(r'^register/$', register, name='register'),
    #take you to profile
    url(r'^profile/$', profile, name='profile'),
    #take you to logout
    url(r'^logout/$', logout, name='logout'),
    #take you to login page
    url(r'^login/$', login, name='login'),
    #will reset your password
    url(r'^password-reset/', include(urls_reset)),
]
