from django.contrib import admin
from django import forms
from .models import project, compiler_run, source_file, derived_file, report_template, report_run

class projectAdminForm(forms.ModelForm):

    class Meta:
        model = project
        fields = '__all__'


class projectAdmin(admin.ModelAdmin):
    form = projectAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(project, projectAdmin)


class compiler_runAdminForm(forms.ModelForm):

    class Meta:
        model = compiler_run
        fields = '__all__'


class compiler_runAdmin(admin.ModelAdmin):
    form = compiler_runAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(compiler_run, compiler_runAdmin)


class source_fileAdminForm(forms.ModelForm):

    class Meta:
        model = source_file
        fields = '__all__'


class source_fileAdmin(admin.ModelAdmin):
    form = source_fileAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'path']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'path']

admin.site.register(source_file, source_fileAdmin)


class derived_fileAdminForm(forms.ModelForm):

    class Meta:
        model = derived_file
        fields = '__all__'


class derived_fileAdmin(admin.ModelAdmin):
    form = derived_fileAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(derived_file, derived_fileAdmin)


class report_templateAdminForm(forms.ModelForm):

    class Meta:
        model = report_template
        fields = '__all__'


class report_templateAdmin(admin.ModelAdmin):
    form = report_templateAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(report_template, report_templateAdmin)


class report_runAdminForm(forms.ModelForm):

    class Meta:
        model = report_run
        fields = '__all__'


class report_runAdmin(admin.ModelAdmin):
    form = report_runAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(report_run, report_runAdmin)


