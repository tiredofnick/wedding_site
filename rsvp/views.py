from django.shortcuts import render_to_response, get_object_or_404
from rsvp.models import Rsvp

def index(request):
	return render_to_response('rsvp/index.html')

def detail(request, rsvp_id):
	r = get_object_or_404(Rsvp, confirmation_code=get(request.POST['confirmation_code']))
	return render_to_response('rsvp/detail.html', {'rsvp': r}, context_instance=RequestContext(r))