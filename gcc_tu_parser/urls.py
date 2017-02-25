#
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include

import gcc_tu_parser.views

urlpatterns = [
    url(r'^files',gcc_tu_parser.views.files,name='files'),
    url(r'^file/(\d+)$',gcc_tu_parser.views.picklefile,name='pickle_file'),
    url(r'^file/(\d+)/(.+)$',gcc_tu_parser.views.file_nodetype,name='node_type'),
    url(r'^func_decls/(\d+)$',gcc_tu_parser.views.func_decls,name='func_decls'),
    url(r'^func_decls/(\d+)/(\d+)$',gcc_tu_parser.views.func_decls2,name='func_decls'),
]

