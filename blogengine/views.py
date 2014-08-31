from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):

	context = RequestContext(request)

	return render_to_response('blogengine/blog_homepage.html', context)
