from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView

from media.models import Photo, PhotoSet

urlpatterns = patterns('',
    url(r'^$',
        view=ListView.as_view(model=Photo),
        name='photo_list'
    ),
    url(r'^(?P<slug>[-\w]+)/$',
        view=DetailView.as_view(model=Photo),
        name='photo_detail'
    ),
    url(r'^sets/$',
        view=ListView.as_view(model=PhotoSet),
        name='photo_set_list'
    ),
    url(r'^sets/(?P<slug>[-\w]+)/$',
        view=DetailView.as_view(model=PhotoSet),
        name='photo_set_detail',
    ),
)
