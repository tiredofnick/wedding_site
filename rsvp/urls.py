from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'rsvp.views.index'),
	(r'^confirm/(?P<rsvp_id>\d+)/$', 'rsvp.views.detail'),
)
