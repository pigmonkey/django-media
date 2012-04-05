from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView

from media.models import Video, VideoSet

urlpatterns = patterns('',
    url(r'^$',
        view=ListView.as_view(model=Video),
        name='video_list'
    ),
    url(r'^(?P<slug>[-\w]+)/$',
        view=DetailView.as_view(model=Video),
        name='video_detail'
    ),
    url(r'^sets/$',
        view=ListView.as_view(model=VideoSet),
        name='video_set_list'
    ),
    url(r'^sets/(?P<slug>[-\w]+)/$',
        view=DetailView.as_view(model=VideoSet),
        name='video_set_detail',
    ),
)
