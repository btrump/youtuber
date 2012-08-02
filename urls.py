from django.conf.urls import patterns, include, url
from youtuber.models import Youtuber

urlpatterns = patterns('youtuber.views',
                       url(r'^$', 'index'),
                       url(r'^(?P<youtuber_id>\d+)/$', 'detail'),
                       url(r'^refresh_data/$', 'refresh_data'),
                       )
