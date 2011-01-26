from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
	return render_to_response('rsvp/index.html')

def detail(request, rsvp_id):
	return HttpResponse("You're looking at rsvp %s." % rsvp_id)