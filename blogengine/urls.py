from django.conf.urls import patterns, url

from blogengine import views

urlpatterns = patterns('',
        
        url(
        	regex=r'^$', 
        	view=views.index, 
        	name='index'
        ),

        url(
        	regex=r'^(?P<slug>[\-\_\w]+)/$',
        	view=views.post_detail,
        	name='post_detail',
        )

)