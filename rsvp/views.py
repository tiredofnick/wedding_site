from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404
from rsvp.models import Rsvp, Attendee, RsvpForm


def index(request):
	if request.method == 'POST':
		rsvp = RsvpForm(request.POST)
		try:
			r = Rsvp.objects.get(confirmation_code=request.POST['confirmation_code'])
		except Rsvp.DoesNotExist:
			raise Http404
		return render_to_response('rsvp/detail.html', {'rsvp': r}, context_instance=RequestContext(request))
	else:
		return render_to_response('rsvp/index.html', context_instance=RequestContext(request))

def detail(request, code):
	r = get_object_or_404(Rsvp, confirmation_code=code)
	return render_to_response('rsvp/detail.html', {'rsvp': r}, context_instance=RequestContext(request))
	
def submit(request):
	return
	