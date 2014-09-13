from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Category

def index(request):

	context = RequestContext(request)

	### start pagination ###
	post_list = Post.objects.order_by('-pub_date') #order all blog posts by published date

	paginator = Paginator(post_list,2) #number of posts that show on home page

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
	### end pagination ###

	### side bar items ###
	popular_posts = Post.objects.order_by('-views')[:5]
	context_dict['popular_posts'] = popular_posts

	cat_list = Category.objects.all()[:8]
	cat_list1 = cat_list[:4]
	cat_list2 = cat_list[5:]
	context_dict['cat_list1'] = cat_list1
	context_dict['cat_list2'] = cat_list2
	### end side bar items ###

	return render_to_response('blogengine/blog_homepage.html', context_dict, context)

def post_detail(request, slug):

	context = RequestContext(request)

	post = Post.objects.get(slug=slug)
	context_dict = {'Post':post}

	### side bar items ###
	popular_posts = Post.objects.order_by('-views')[:5]
	context_dict['popular_posts'] = popular_posts

	cat_list = Category.objects.all()[:8]
	cat_list1 = cat_list[:4]
	cat_list2 = cat_list[5:]
	context_dict['cat_list1'] = cat_list1
	context_dict['cat_list2'] = cat_list2
	### end side bar items ###

	return render_to_response('blogengine/blog_detail.html', context_dict, context)

def category_detail(request, slug):
	context = RequestContext(request)

	cat_detail = Category.objects.get(cat_slug=slug)
	context_dict = {'cat_detail':cat_detail}

	### start pagination post list ###
	post_cat_list = Post.objects.filter(category=cat_detail).order_by('-pub_date') #retrieve all blog posts in category in pub_date order

	paginator = Paginator(post_cat_list,2) #number of posts that show on each page

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
	### end pagination ###


	### side bar items ###
	popular_posts = Post.objects.order_by('-views')[:5]
	context_dict['popular_posts'] = popular_posts

	cat_list = Category.objects.all()[:8]
	cat_list1 = cat_list[:4]
	cat_list2 = cat_list[5:]
	context_dict['cat_list1'] = cat_list1
	context_dict['cat_list2'] = cat_list2
	### end side bar items ###

	return render_to_response('blogengine/category_detail.html', context_dict, context)