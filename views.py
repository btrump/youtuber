from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from youtuber.models import Youtuber
import json

def index(request):
    NUM_LIST_ITEMS = 5
    videos = Youtuber.objects.all().order_by('-publish_start')[:NUM_LIST_ITEMS]
    data = {
            'videos':       videos[1:5],
            'latest_video': videos[0],
            'embed_html':   videos[0].build_html_embed(580, 320)
            }
    context = RequestContext(request, data)
    return render_to_response('youtuber/index.html', context)

def detail(request, youtuber_id):
    video = get_object_or_404(Youtuber, pk=youtuber_id)
    return render_to_response('youtuber/detail.html', {'video': video},
                              context_instance=RequestContext(request))

def refresh_data(request):
    video = Youtuber()
    data = video.initialize(request.REQUEST['video_url'])
    json_data = {
                    'video_url':        data.video_url,
                    'provider_url':     data.provider_url,
                    'thumbnail_url':    data.thumbnail_url,
                    'title':            data.title,
                    'author_name':      data.author_name,
                    'author_url':       data.author_url,
                    'video_code':       data.video_code,
                }

    return HttpResponse(json.dumps(json_data), mimetype='application/json')
