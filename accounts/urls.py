from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile
from accounts import urls_reset


urlpatterns = [
    # Takes you to registration page
    url(r'^register/$', registration, name="registration"),
    # Takes you to profile
    url(r'^profile/$', user_profile, name="profile"),
    # Tskes you to logout
    url(r'^logout/$', logout, name="logout"),
    # Takes you to login
    url(r'^login/$', login, name="login"),
    # Will reset your password
    url(r'^password-reset/', include(urls_reset))
]
