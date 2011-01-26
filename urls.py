from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^rsvp/$', 'rsvp.views.index'),
	(r'^rsvp/(?P<rsvp_id>\d+)/$', 'rsvp.views.detail'),
    (r'^admin/', include(admin.site.urls)),
)
