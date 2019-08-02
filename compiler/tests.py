import unittest
from django.urls import reverse
from django.test import Client
from .models import project, compiler_run, source_file, derived_file, report_template, report_run
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_project(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return project.objects.create(**defaults)


def create_compiler_run(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "project" not in defaults:
        defaults["project"] = create_project()
    return compiler_run.objects.create(**defaults)


def create_source_file(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["path"] = "path"
    defaults.update(**kwargs)
    if "project" not in defaults:
        defaults["project"] = create_project()
    return source_file.objects.create(**defaults)


def create_derived_file(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "source" not in defaults:
        defaults["source"] = create_source_file()
    return derived_file.objects.create(**defaults)


def create_report_template(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return report_template.objects.create(**defaults)


def create_report_run(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "source" not in defaults:
        defaults["source"] = create_compiler_run()
    return report_run.objects.create(**defaults)


class projectViewTest(unittest.TestCase):
    '''
    Tests for project
    '''
    def setUp(self):
        self.client = Client()

    def test_list_project(self):
        url = reverse('compiler_project_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_project(self):
        url = reverse('compiler_project_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_project(self):
        project = create_project()
        url = reverse('compiler_project_detail', args=[project.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_project(self):
        project = create_project()
        data = {
            "name": "name",
        }
        url = reverse('compiler_project_update', args=[project.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class compiler_runViewTest(unittest.TestCase):
    '''
    Tests for compiler_run
    '''
    def setUp(self):
        self.client = Client()

    def test_list_compiler_run(self):
        url = reverse('compiler_compiler_run_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_compiler_run(self):
        url = reverse('compiler_compiler_run_create')
        data = {
            "name": "name",
            "project": create_project().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_compiler_run(self):
        compiler_run = create_compiler_run()
        url = reverse('compiler_compiler_run_detail', args=[compiler_run.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_compiler_run(self):
        compiler_run = create_compiler_run()
        data = {
            "name": "name",
            "project": create_project().pk,
        }
        url = reverse('compiler_compiler_run_update', args=[compiler_run.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class source_fileViewTest(unittest.TestCase):
    '''
    Tests for source_file
    '''
    def setUp(self):
        self.client = Client()

    def test_list_source_file(self):
        url = reverse('compiler_source_file_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_source_file(self):
        url = reverse('compiler_source_file_create')
        data = {
            "name": "name",
            "path": "path",
            "project": create_project().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_source_file(self):
        source_file = create_source_file()
        url = reverse('compiler_source_file_detail', args=[source_file.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_source_file(self):
        source_file = create_source_file()
        data = {
            "name": "name",
            "path": "path",
            "project": create_project().pk,
        }
        url = reverse('compiler_source_file_update', args=[source_file.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class derived_fileViewTest(unittest.TestCase):
    '''
    Tests for derived_file
    '''
    def setUp(self):
        self.client = Client()

    def test_list_derived_file(self):
        url = reverse('compiler_derived_file_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_derived_file(self):
        url = reverse('compiler_derived_file_create')
        data = {
            "name": "name",
            "source": create_source_file().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_derived_file(self):
        derived_file = create_derived_file()
        url = reverse('compiler_derived_file_detail', args=[derived_file.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_derived_file(self):
        derived_file = create_derived_file()
        data = {
            "name": "name",
            "source": create_source_file().pk,
        }
        url = reverse('compiler_derived_file_update', args=[derived_file.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class report_templateViewTest(unittest.TestCase):
    '''
    Tests for report_template
    '''
    def setUp(self):
        self.client = Client()

    def test_list_report_template(self):
        url = reverse('compiler_report_template_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_report_template(self):
        url = reverse('compiler_report_template_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_report_template(self):
        report_template = create_report_template()
        url = reverse('compiler_report_template_detail', args=[report_template.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_report_template(self):
        report_template = create_report_template()
        data = {
            "name": "name",
        }
        url = reverse('compiler_report_template_update', args=[report_template.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class report_runViewTest(unittest.TestCase):
    '''
    Tests for report_run
    '''
    def setUp(self):
        self.client = Client()

    def test_list_report_run(self):
        url = reverse('compiler_report_run_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_report_run(self):
        url = reverse('compiler_report_run_create')
        data = {
            "name": "name",
            "source": create_compiler_run().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_report_run(self):
        report_run = create_report_run()
        url = reverse('compiler_report_run_detail', args=[report_run.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_report_run(self):
        report_run = create_report_run()
        data = {
            "name": "name",
            "source": create_compiler_run().pk,
        }
        url = reverse('compiler_report_run_update', args=[report_run.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


