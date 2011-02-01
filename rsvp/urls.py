from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^rsvp/$', 'rsvp.views.index'),
	(r'^rsvp/(?P<rsvp_id>\d+)/$', 'rsvp.views.detail'),
)
