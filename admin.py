from youtuber.models import Youtuber
from django.contrib import admin

class YoutuberAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None, {'fields': ['video_url', 'title', 'thumbnail_url', 'published_on']}),
                 (u"""Advanced Data (don't change unless you know what you're doing!)""", {'fields': ['provider_url', 'author_name', 'author_url', 'video_code'], 'classes':['collapse']}),
                 # ('Date Information', {'fields': ['published_on', 'modified_on', 'created_on'], 'classes':['collapse']}),
                 ]
    list_display = ('title', 'created_on', 'published_on', 'was_published_recently')
    list_filter = ['published_on']
    date_hierarchy = 'published_on'
    search_fields = ['title']
    
admin.site.register(Youtuber, YoutuberAdmin)