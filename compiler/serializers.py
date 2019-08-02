from . import models

from rest_framework import serializers


class projectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.project
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class compiler_runSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.compiler_run
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class source_fileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.source_file
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'path', 
        )


class derived_fileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.derived_file
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class report_templateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.report_template
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class report_runSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.report_run
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


