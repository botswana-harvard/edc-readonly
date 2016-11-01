from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.apps import apps as django_apps
from django.shortcuts import render

from edc_base.view_mixins import EdcBaseViewMixin

from example.models import MyModel
from django.conf import settings


class ReadOnlyView(EdcBaseViewMixin, TemplateView, FormView):

    def __init__(self):
        self.context = {}
        self.template_name = 'read_only_form.html'

    def class_for_name(self, module_name, class_name):
        # load the module, will raise ImportError if module cannot be loaded
        m = __import__(module_name, globals(), locals(), class_name)
        # get the class, will raise AttributeError if class cannot be found
        c = getattr(m, class_name)
        return c

    def get(self, request, *args, **kwargs):
        model_instance = None
        model_pk = kwargs.get('pk')
        app_label = kwargs.get('app_label')
        model_name = kwargs.get('model_name')
        form_module = kwargs.get('form_module')
        form_class_str = kwargs.get('form_class_str')
        mv = app_label + '.' + model_name
        model = django_apps.get_model(mv)
        from_class = self.class_for_name(form_module, form_class_str)
        try:
            model_instance = model.objects.get(pk=model_pk)
        except model.DoesNotExist:
            model_instance = None
        form = from_class(model_instance.__dict__)
        readonly_fields = form.fields
        for field in (field for name, field in form.fields.items() if name in readonly_fields):
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True
        self.context.update({
            'model_instance': model_instance,
            'project_name': settings.PROJECT_TITLE,
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
        my_model = None
        try:
            my_model = MyModel.objects.get(id=2)
        except:
            my_model = MyModel.objects.create(id=2, my_first_field='i was playing soccer', my_second_field='no its the third time')
        self.context.update({
            'my_model': my_model.__class__.__name__,
            'app_label': my_model._meta.app_label,
            'project_name': settings.PROJECT_TITLE,
            'my_model_pk': my_model.pk,
            'form_class_str': 'MyModelForm',
            'form_module': "example.forms"
        })
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        self.context.update({
        })
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        return super(ReadOnlyView, self).get_context_data(**kwargs)
