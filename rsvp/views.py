from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from rsvp.models import Rsvp


def index(request):
	return render_to_response('rsvp/index.html', context_instance=RequestContext(request))

def detail(request):
	r = get_object_or_404(Rsvp, confirmation_code=request.POST['confirmation_code'])
	return render_to_response('rsvp/detail.html', {'rsvp': r})
	#try:
	#	r = request.POST['confirmation_code']
	#	return render_to_response('rsvp/detail.html', {'rsvp': r})