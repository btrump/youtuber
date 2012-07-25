from youtuber.models import Youtuber
from django.contrib import admin

class YoutuberAdmin(admin.ModelAdmin):
    """
    fieldsets = [
                 (None, {'fields': ['question']}),
                 ('Date Information', {'fields': ['pub_date']}),
                 ]
    """
    exclude = ('provider_url','author_url','created_on','modified_on','author_name')
    list_display = ('title', 'created_on', 'published_on', 'was_published_recently')
    list_filter = ['published_on']
    date_hierarchy = 'published_on'
    search_fields = ['title']
    
admin.site.register(Youtuber, YoutuberAdmin)