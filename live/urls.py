from django.conf.urls import *
from live.forms import new_update
from live.views import UpdateListView, updates_after

urlpatterns = patterns('',
    url(r'^$', UpdateListView.as_view(), name='update-list'),
    url(r'^updates-after/(?P<id>\d+)/$', updates_after),
    url(r'^add/$', new_update)
)