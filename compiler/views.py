from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import project, compiler_run, source_file, derived_file, report_template, report_run
from .forms import projectForm, compiler_runForm, source_fileForm, derived_fileForm, report_templateForm, report_runForm


class projectListView(ListView):
    model = project


class projectCreateView(CreateView):
    model = project
    form_class = projectForm


class projectDetailView(DetailView):
    model = project


class projectUpdateView(UpdateView):
    model = project
    form_class = projectForm


class compiler_runListView(ListView):
    model = compiler_run


class compiler_runCreateView(CreateView):
    model = compiler_run
    form_class = compiler_runForm


class compiler_runDetailView(DetailView):
    model = compiler_run


class compiler_runUpdateView(UpdateView):
    model = compiler_run
    form_class = compiler_runForm


class source_fileListView(ListView):
    model = source_file


class source_fileCreateView(CreateView):
    model = source_file
    form_class = source_fileForm


class source_fileDetailView(DetailView):
    model = source_file


class source_fileUpdateView(UpdateView):
    model = source_file
    form_class = source_fileForm


class derived_fileListView(ListView):
    model = derived_file


class derived_fileCreateView(CreateView):
    model = derived_file
    form_class = derived_fileForm


class derived_fileDetailView(DetailView):
    model = derived_file


class derived_fileUpdateView(UpdateView):
    model = derived_file
    form_class = derived_fileForm


class report_templateListView(ListView):
    model = report_template


class report_templateCreateView(CreateView):
    model = report_template
    form_class = report_templateForm


class report_templateDetailView(DetailView):
    model = report_template


class report_templateUpdateView(UpdateView):
    model = report_template
    form_class = report_templateForm


class report_runListView(ListView):
    model = report_run


class report_runCreateView(CreateView):
    model = report_run
    form_class = report_runForm


class report_runDetailView(DetailView):
    model = report_run


class report_runUpdateView(UpdateView):
    model = report_run
    form_class = report_runForm

