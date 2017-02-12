#
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include

import gcc_tu_parser.views

urlpatterns = [
    url(r'^files',gcc_tu_parser.views.files,name='files'),
    url(r'^file/(.+)$',gcc_tu_parser.views.picklefile,name='pickle_file')
]

