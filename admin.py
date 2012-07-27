from youtuber.models import Youtuber
from django.contrib import admin

class YoutuberAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None, {'fields': ['video_url', 'title', 'thumbnail_url']}),
                 ('Date Information', {'fields': ['publish_start', 'publish_end']}),
                 (u"""Advanced Data (don't change unless you know what you're doing!)""", {'fields': ['provider_url', 'author_name', 'author_url', 'video_code'], 'classes':['collapse']}),
                 ]
    list_display = ('title', 'publish_start', 'publish_end', 'is_active', 'was_published_recently')
    list_filter = ['publish_start']
    date_hierarchy = 'publish_start'
    search_fields = ['title']
    
admin.site.register(Youtuber, YoutuberAdmin)