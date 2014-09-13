from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('blogengine.urls', namespace='blogengine')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^about/$',
            TemplateView.as_view(template_name="pages/about.html"),
            name="about"
    ),
)
