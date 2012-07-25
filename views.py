from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from youtuber.models import Youtuber

def index(request):
    videos = Youtuber.objects.all().order_by('-created_on')[:5]
    context = RequestContext(request, {'videos': videos})
    return render_to_response('youtuber/index.html', context)

def detail(request, youtuber_id):
    video = get_object_or_404(Youtuber, pk=youtuber_id)
    return render_to_response('youtuber/detail.html', {'video': video},
                              context_instance=RequestContext(request))