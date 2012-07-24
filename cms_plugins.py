from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

class YoutuberPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _('Youtuber Plugin')
    render_template = 'polls/plugin.html'
    
    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context
        
plugin_pool.register_plugin(YoutuberPlugin)