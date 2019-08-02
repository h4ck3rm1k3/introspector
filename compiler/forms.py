from django import forms
from .models import project, compiler_run, source_file, derived_file, report_template, report_run


class projectForm(forms.ModelForm):
    class Meta:
        model = project
        fields = ['name']


class compiler_runForm(forms.ModelForm):
    class Meta:
        model = compiler_run
        fields = ['name', 'project']


class source_fileForm(forms.ModelForm):
    class Meta:
        model = source_file
        fields = ['name', 'path', 'project']


class derived_fileForm(forms.ModelForm):
    class Meta:
        model = derived_file
        fields = ['name', 'source']


class report_templateForm(forms.ModelForm):
    class Meta:
        model = report_template
        fields = ['name']


class report_runForm(forms.ModelForm):
    class Meta:
        model = report_run
        fields = ['name', 'source']


