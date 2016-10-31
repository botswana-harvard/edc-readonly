from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.apps import apps as django_apps
from django.shortcuts import render

from edc_base.view_mixins import EdcBaseViewMixin

from example.models import MyModel
from example.forms import MyModelForm


class ReadOnlyView(EdcBaseViewMixin, TemplateView, FormView):

    def __init__(self):
        self.context = {}
        self.template_name = 'read_only_form.html'

    def get(self, request, *args, **kwargs):
        model_instance = None
        model_pk = kwargs.get('pk')
        app_label = kwargs.get('app_label')
        model_name = kwargs.get('model_name')
        mv = app_label + '.' + model_name
        model = django_apps.get_model(mv)
        try:
            model_instance = model.objects.get(pk=model_pk)
        except model.DoesNotExist:
            model_instance = None
        form = MyModelForm(model_instance.__dict__)
        readonly_fields = form.fields
        for field in (field for name, field in form.fields.items() if name in readonly_fields):
            field.widget.attrs['readonly'] = 'true'
        self.context.update({
            'model_instance': model_instance,
            'project_name': 'EDC Read Only',
            'model_name': model._meta.verbose_name,
            'form': form
        })
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        self.context.update({
        })
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        return super(ReadOnlyView, self).get_context_data(**kwargs)


class HomeView(EdcBaseViewMixin, TemplateView, FormView):

    def __init__(self):
        self.context = {}
        self.template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        my_model = MyModel.objects.all()[0]
        self.context.update({
            'my_model': my_model.__class__.__name__,
            'app_label': my_model._meta.app_label,
            'project_name': 'EDC Read Only',
            'my_model_pk': my_model.pk,
            'formm': 'MyModelForm'
        })
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        self.context.update({
        })
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        return super(ReadOnlyView, self).get_context_data(**kwargs)
