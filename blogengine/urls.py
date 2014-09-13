from django.conf.urls import patterns, url

from blogengine import views

urlpatterns = patterns('',
        
        url(
        	regex=r'^$', 
        	view=views.index, 
        	name='index'
        ),

        url(
        	regex=r'^post/(?P<slug>[\-\_\w]+)/$',
        	view=views.post_detail,
        	name='post_detail',
        ),

        url(
                regex=r'^category/(?P<slug>[\-\_\w]+)/$',
                view=views.category_detail,
                name='category_detail',
        )

)