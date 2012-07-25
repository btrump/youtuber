from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from youtuber.menu import YoutuberMenu
from django.utils.translation import ugettext_lazy as _

class YoutuberApp(CMSApp):
    name = _('Youtuber App') # give your app a name, this is required
    urls = ['youtuber.urls'] # link your app to url configuration(s)
    menus = [YoutuberMenu] # attach a CMSAttachMenu to this apphook.

apphook_pool.register(YoutuberApp) # register your app