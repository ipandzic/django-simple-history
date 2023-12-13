from __future__ import unicode_literals

from django.urls import re_path
from django.contrib import admin

from simple_history.tests.view import (
    BucketDataRegisterRequestUserCreate,
    BucketDataRegisterRequestUserDetail,
    PollCreate,
    PollDelete,
    PollDetail,
    PollList,
    PollUpdate
)
from . import other_admin

admin.autodiscover()

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^other-admin/', other_admin.site.urls),
    re_path(r'^bucket_data/add/$',
        BucketDataRegisterRequestUserCreate.as_view(),
        name='bucket_data-add'),
    re_path(r'^bucket_data/(?P<pk>[0-9]+)/$',
        BucketDataRegisterRequestUserDetail.as_view(),
        name='bucket_data-detail'),
    re_path(r'^poll/add/$', PollCreate.as_view(), name='poll-add'),
    re_path(r'^poll/(?P<pk>[0-9]+)/$', PollUpdate.as_view(), name='poll-update'),
    re_path(r'^poll/(?P<pk>[0-9]+)/delete/$', PollDelete.as_view(),
        name='poll-delete'),
    re_path(r'^polls/(?P<pk>[0-9]+)/$', PollDetail.as_view(), name='poll-detail'),
    re_path(r'^polls/$', PollList.as_view(), name='poll-list')
]
