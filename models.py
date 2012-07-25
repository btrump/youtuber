from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
import json, httplib, datetime

class Youtuber(models.Model):
    video_url = models.URLField(max_length=200)
    provider_url = models.URLField(max_length=200)
    thumbnail_url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    author_url = models.URLField(max_length=200)
    created_on = models.DateTimeField(default=timezone.now())
    modified_on = models.DateTimeField(default=timezone.now())
    published_on = models.DateTimeField(null=True)
    html = models.TextField()
    
    def __unicode__(self):
        return self.title

    def initialize(self, video_url='https://www.youtube.com/watch?v=827ZSLiUI9o'):
        """Takes a Youtube video URL and calls refresh_data() to pull data from Youtube."""
        self.video_url = video_url
        self.refresh_data()
        
    def was_published_recently(self):
        """Returns True if the publish date is fewer than a day ago."""
        if type(self.published_on) is datetime.datetime:
            return (self.published_on >= timezone.now() - datetime.timedelta(days=1)) 
        else:
            return False
    was_published_recently.boolean = True
    was_published_recently.admin_order_field = 'published_on'
    was_published_recently.short_description = 'Published recently?'
    
    def refresh_data(self):
        """Updates the information in the Youtuber object with data from Youtube."""
        yt_domain = 'www.youtube.com'
        qs = '?format=json&url='
        qs += self.video_url
        request = '/oembed' + qs
        conn = httplib.HTTPConnection(yt_domain)
        conn.request('GET', request)
        response = conn.getresponse()
        json_data = json.loads(response.read())
        self.provider_url = json_data['provider_url']
        self.thumbnail_url = json_data['thumbnail_url']
        self.title = json_data['title']
        self.author_name = json_data['author_name']
        self.author_url = json_data['author_url']
        self.html = json_data['html']
        
class YoutuberPlugin(CMSPlugin):
    # poll = models.ForeignKey(Poll, related_name='plugins')
    video = models.ForeignKey(Youtuber, related_name='plugins')

    def __unicode__(self):
      return self.video.title