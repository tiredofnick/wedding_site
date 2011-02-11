from django.conf.urls.defaults import *

urlpatterns = patterns('rsvp.views',
    (r'^$', 'index'),
	(r'^confirm/$', 'detail'),
	(r'^confirm/(?P<rsvp_id>\d+)/$', 'detail'),
	(r'^(?P<rsvp_id>\d+)/submit/$', 'submit'),
)
