__author__ = 'sparky'
from django.conf.urls import patterns, include, url
from views import EView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'poker_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'eform/$', EView.as_view()),
)