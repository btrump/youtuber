from django.db import models
from django.utils import timezone
import json, httplib, datetime

class Youtuber(models.Model):
    provider_url = models.CharField(max_length=200)
    thumbnail_url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    author_url = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    
    def __unicode__(self):
        return('%s - %s', self.author_name, self.title)


"""
<oembed>
<provider_url>http://www.youtube.com/</provider_url>
<thumbnail_url>http://i2.ytimg.com/vi/i3Jv9fNPjgk/hqdefault.jpg</thumbnail_url>
<title>AZEALIA BANKS - 212 FT. LAZY JAY</title>
<html>
<iframe width="480" height="270" src="http://www.youtube.com/embed/i3Jv9fNPjgk?fs=1&feature=oembed" frameborder="0" allowfullscreen></iframe>
</html>
<author_name>AzealiaBanks</author_name>
<height>270</height>
<thumbnail_width>480</thumbnail_width>
<width>480</width>
<version>1.0</version>
<author_url>http://www.youtube.com/user/AzealiaBanks</author_url>
<provider_name>YouTube</provider_name>
<type>video</type>
<thumbnail_height>360</thumbnail_height>
</oembed>
"""