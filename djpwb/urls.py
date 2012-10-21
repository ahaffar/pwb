from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('djpwb.pwb.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'HelloWorld', name='hello'),
    url(r'^date/$', 'current_date'),
    url(r'^$', 'home', name='index'),
    url(r'^date/plus/([0-6][0-9])/$', 'datetime_offset'),
    url(r'^polls?/$', 'index'),
    url(r'^polls?/(?P<poll_id>\d{1,2})/$', 'details', name='poll-url'),
    url(r'^polls?/(?P<poll_id>\d{2})/results/$', 'results'),
    url(r'^polls?/(?P<poll_id>\d{2})/votes/$', 'votes'),
    url(r'^logout/$','logout'),
    url(r'^ua/$','user_agent'),
    url(r'^ip/$','ip'),
    url(r'^meta/$','display_meta'),
    url(r'^search_form/$','search_form', name='search_form'),
    url(r'^search/$','search', name='search_results'),
    url(r'^contact_us/$','contact', name='contacts'),	
    url(r'^resume/$','resume', name='resumes')
)

