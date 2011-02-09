from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'rsvp.views.index'),
	(r'^confirm/$', 'rsvp.views.detail'),
	(r'^confirm/(?P<rsvp_id>\d+)/$', 'rsvp.views.detail'),
	(r'^submit/$', 'rsvp.views.submit'),
)
