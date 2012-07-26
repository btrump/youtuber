from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.forms import ModelForm
import json, httplib, datetime, re

class Youtuber(models.Model):
    video_url = models.URLField(max_length=200)
    provider_url = models.URLField(max_length=200)
    thumbnail_url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    author_url = models.URLField(max_length=200)
    video_code = models.CharField(max_length=50)
    created_on = models.DateTimeField(default=timezone.now())
    modified_on = models.DateTimeField(default=timezone.now())
    published_on = models.DateTimeField(null=True, blank=True)
    
    def __unicode__(self):
        return self.title

    def initialize(self, video_url='https://www.youtube.com/watch?v=827ZSLiUI9o'):
        """
		Takes a Youtube video URL and calls refresh_data() to pull data from Youtube.
        """
        self.video_url = video_url
        return self.refresh_data()
        
    def was_published_recently(self):
        """
		Returns True if the publish date is fewer than a day ago.
        """
        if type(self.published_on) is datetime.datetime:
            return (self.published_on >= timezone.now() - datetime.timedelta(days=1)) 
        else:
            return False
    was_published_recently.boolean = True
    was_published_recently.admin_order_field = 'published_on'
    was_published_recently.short_description = 'Published recently?'
    
    def build_html_embed(self, width=420, height=263):
        """
		Builds an HTML embed code using an iframe and passed or default WxH dimensions.
        """
        url = '%sembed/%s?fs=1' % (self.provider_url, self.video_code)
        html = '<iframe width="%i" height="%i" src="%s" frameborder="0" allowfullscreen></iframe>' % (width, height, url)
        return html
    
    def refresh_data(self):
        """
		Updates the information in the Youtuber object with data from Youtube.
        """
        # Parse the supplied video_url string to:
        # 1.  Strip any get variables after video ('v') from query string
        # 2.  Get the video code
        match = re.search('(.+\?v=)(\w+).*', self.video_url)
        self.video_url = match.group(1) + match.group(2)
        self.video_code = match.group(2)
        
        # Get the oembed JSON data from YouTube
        yt_domain = 'www.youtube.com'
        qs = '?format=json&url='
        qs += self.video_url
        request = '/oembed' + qs
        conn = httplib.HTTPConnection(yt_domain)
        conn.request('GET', request)
        response = conn.getresponse()
        json_data = json.loads(response.read())
        
        # Update current object
        self.provider_url = json_data['provider_url']
        self.thumbnail_url = json_data['thumbnail_url']
        self.title = json_data['title'].title()
        self.author_name = json_data['author_name']
        self.author_url = json_data['author_url']
        return self
        
class YoutuberPlugin(CMSPlugin):
    video = models.ForeignKey('youtuber.Youtuber', related_name='plugins')

    def __unicode__(self):
      return self.video.title
