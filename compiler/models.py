from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import TextField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class project(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('compiler_project_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('compiler_project_update', args=(self.slug,))


class compiler_run(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    project = models.ForeignKey(
        'compiler.project',
        on_delete=models.CASCADE, related_name="compiler_runs", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('compiler_compiler_run_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('compiler_compiler_run_update', args=(self.slug,))


class source_file(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    path = models.TextField(max_length=4096)

    # Relationship Fields
    project = models.ForeignKey(
        'compiler.project',
        on_delete=models.CASCADE, related_name="source_files", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('compiler_source_file_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('compiler_source_file_update', args=(self.slug,))


class derived_file(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    source = models.ForeignKey(
        'compiler.source_file',
        on_delete=models.CASCADE, related_name="derived_files", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('compiler_derived_file_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('compiler_derived_file_update', args=(self.slug,))


class report_template(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('compiler_report_template_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('compiler_report_template_update', args=(self.slug,))


class report_run(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    source = models.ForeignKey(
        'compiler.compiler_run',
        on_delete=models.CASCADE, related_name="report_runs", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('compiler_report_run_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('compiler_report_run_update', args=(self.slug,))


