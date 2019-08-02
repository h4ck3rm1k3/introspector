from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'project', api.projectViewSet)
router.register(r'compiler_run', api.compiler_runViewSet)
router.register(r'source_file', api.source_fileViewSet)
router.register(r'derived_file', api.derived_fileViewSet)
router.register(r'report_template', api.report_templateViewSet)
router.register(r'report_run', api.report_runViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for project
    path('compiler/project/', views.projectListView.as_view(), name='compiler_project_list'),
    path('compiler/project/create/', views.projectCreateView.as_view(), name='compiler_project_create'),
    path('compiler/project/detail/<slug:slug>/', views.projectDetailView.as_view(), name='compiler_project_detail'),
    path('compiler/project/update/<slug:slug>/', views.projectUpdateView.as_view(), name='compiler_project_update'),
)

urlpatterns += (
    # urls for compiler_run
    path('compiler/compiler_run/', views.compiler_runListView.as_view(), name='compiler_compiler_run_list'),
    path('compiler/compiler_run/create/', views.compiler_runCreateView.as_view(), name='compiler_compiler_run_create'),
    path('compiler/compiler_run/detail/<slug:slug>/', views.compiler_runDetailView.as_view(), name='compiler_compiler_run_detail'),
    path('compiler/compiler_run/update/<slug:slug>/', views.compiler_runUpdateView.as_view(), name='compiler_compiler_run_update'),
)

urlpatterns += (
    # urls for source_file
    path('compiler/source_file/', views.source_fileListView.as_view(), name='compiler_source_file_list'),
    path('compiler/source_file/create/', views.source_fileCreateView.as_view(), name='compiler_source_file_create'),
    path('compiler/source_file/detail/<slug:slug>/', views.source_fileDetailView.as_view(), name='compiler_source_file_detail'),
    path('compiler/source_file/update/<slug:slug>/', views.source_fileUpdateView.as_view(), name='compiler_source_file_update'),
)

urlpatterns += (
    # urls for derived_file
    path('compiler/derived_file/', views.derived_fileListView.as_view(), name='compiler_derived_file_list'),
    path('compiler/derived_file/create/', views.derived_fileCreateView.as_view(), name='compiler_derived_file_create'),
    path('compiler/derived_file/detail/<slug:slug>/', views.derived_fileDetailView.as_view(), name='compiler_derived_file_detail'),
    path('compiler/derived_file/update/<slug:slug>/', views.derived_fileUpdateView.as_view(), name='compiler_derived_file_update'),
)

urlpatterns += (
    # urls for report_template
    path('compiler/report_template/', views.report_templateListView.as_view(), name='compiler_report_template_list'),
    path('compiler/report_template/create/', views.report_templateCreateView.as_view(), name='compiler_report_template_create'),
    path('compiler/report_template/detail/<slug:slug>/', views.report_templateDetailView.as_view(), name='compiler_report_template_detail'),
    path('compiler/report_template/update/<slug:slug>/', views.report_templateUpdateView.as_view(), name='compiler_report_template_update'),
)

urlpatterns += (
    # urls for report_run
    path('compiler/report_run/', views.report_runListView.as_view(), name='compiler_report_run_list'),
    path('compiler/report_run/create/', views.report_runCreateView.as_view(), name='compiler_report_run_create'),
    path('compiler/report_run/detail/<slug:slug>/', views.report_runDetailView.as_view(), name='compiler_report_run_detail'),
    path('compiler/report_run/update/<slug:slug>/', views.report_runUpdateView.as_view(), name='compiler_report_run_update'),
)

