from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import RedirectView
from live.views import logout_view

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', RedirectView.as_view(url='/live/', permanent=False)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'live/login.html'}),
    url(r'^accounts/logout/$', logout_view),
    url(r'^live/', include('live.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
