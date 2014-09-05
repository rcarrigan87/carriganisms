from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post

def index(request):

	context = RequestContext(request)

	post_list = Post.objects.order_by('-pub_date') #order all blog posts by published date

	paginator = Paginator(post_list,2) #show 5 blog posts

	page = request.GET.get('page')

	try:
		post = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		post = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		post = paginator.page(paginator.num_pages)

	context_dict = {'posts':post}

	return render_to_response('blogengine/blog_homepage.html', context_dict, context)

def post_detail(request, slug):

	context = RequestContext(request)

	post = Post.objects.get(slug=slug)

	context_dict = {'Post':post}

	return render_to_response('blogengine/blog_detail.html', context_dict, context)