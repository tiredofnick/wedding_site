from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'rsvp.views.index'),
	(r'^(?P<rsvp_id>\d+)/$', 'rsvp.views.detail'),
)
