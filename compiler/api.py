from . import models
from . import serializers
from rest_framework import viewsets, permissions


class projectViewSet(viewsets.ModelViewSet):
    """ViewSet for the project class"""

    queryset = models.project.objects.all()
    serializer_class = serializers.projectSerializer
    permission_classes = [permissions.IsAuthenticated]


class compiler_runViewSet(viewsets.ModelViewSet):
    """ViewSet for the compiler_run class"""

    queryset = models.compiler_run.objects.all()
    serializer_class = serializers.compiler_runSerializer
    permission_classes = [permissions.IsAuthenticated]


class source_fileViewSet(viewsets.ModelViewSet):
    """ViewSet for the source_file class"""

    queryset = models.source_file.objects.all()
    serializer_class = serializers.source_fileSerializer
    permission_classes = [permissions.IsAuthenticated]


class derived_fileViewSet(viewsets.ModelViewSet):
    """ViewSet for the derived_file class"""

    queryset = models.derived_file.objects.all()
    serializer_class = serializers.derived_fileSerializer
    permission_classes = [permissions.IsAuthenticated]


class report_templateViewSet(viewsets.ModelViewSet):
    """ViewSet for the report_template class"""

    queryset = models.report_template.objects.all()
    serializer_class = serializers.report_templateSerializer
    permission_classes = [permissions.IsAuthenticated]


class report_runViewSet(viewsets.ModelViewSet):
    """ViewSet for the report_run class"""

    queryset = models.report_run.objects.all()
    serializer_class = serializers.report_runSerializer
    permission_classes = [permissions.IsAuthenticated]


