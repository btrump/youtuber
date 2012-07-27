from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from youtuber.models import YoutuberPlugin
from youtuber.models import Youtuber
from django.utils.translation import ugettext as _

class YoutuberPlugin(CMSPluginBase):
    model = YoutuberPlugin
    name = _('Youtuber Plugin')
    render_template = 'youtuber/plugin.html'
    
    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['current_video'] = Youtuber.objects.get(pk=1)
        return context
        
plugin_pool.register_plugin(YoutuberPlugin)