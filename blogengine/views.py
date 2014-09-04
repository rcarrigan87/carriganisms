from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from .models import Post

def index(request):

	context = RequestContext(request)

	post_list = Post.objects.order_by('-pub_date')[:5]

	context_dict = {'posts':post_list}

	return render_to_response('blogengine/blog_homepage.html', context_dict, context)

def post_detail(request, slug):

	context = RequestContext(request)

	post = Post.objects.get(slug=slug)

	context_dict = {'Post':post}

	return render_to_response('blogengine/blog_detail.html', context_dict, context)