from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from youtuber.models import YoutuberPlugin
from youtuber.models import Youtuber
from django.utils.translation import ugettext as _
from random import choice
import datetime

class YoutuberPlugin(CMSPluginBase):
    model = YoutuberPlugin
    name = _('Youtuber Frontpage Video')
    render_template = 'youtuber/plugin.html'
    
    def render(self, context, instance, placeholder):
        """
        Choose a random video from the five most recent active videos
        """
        context['instance'] = instance
        active_videos = Youtuber.objects.filter(publish_start__lte=datetime.datetime.now()).filter(publish_end__gte=datetime.datetime.now())
        if len(active_videos) > 0:
            context['video'] = choice(active_videos)
        else:
            context['video'] = None
        return context
        
plugin_pool.register_plugin(YoutuberPlugin)