from django.apps import apps as django_apps
from django.contrib.auth import get_permission_codename
# from django.contrib import messages


class ReadOnlyAdminMixin:
    """Disables all editing capabilities."""

    @property
    def readonly_auth_group(self):
        """Returns a group name for read only permissions."""
        app_config = django_apps.get_app_config('edc_readonly_admin')
        return app_config.readonly_auth_group_name

    def readonly_group(self, request):
        """Returns True if a user belongs to a ground with read only permissions."""
        groups = [x.name for x in request.user.groups.all()]
        if self.readonly_auth_group in groups:
            return True
        return False

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = []
        if self.readonly_group(request):
            for field in self.get_fields(request, obj):
                readonly_fields.append(field)
            return list(set(readonly_fields))
        return self.readonly_fields

    def has_add_permission(self, request):
        if self.readonly_group(request):
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        if self.readonly_group(request):
            return False
        else:
            opts = self.opts
            codename = get_permission_codename('delete', opts)
            return request.user.has_perm("%s.%s" % (opts.app_label, codename))

    def save_model(self, request, obj, form, change):
        if self.readonly_group(request):
            pass
        else:
            super(ReadOnlyAdminMixin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        if self.readonly_group(request):
            pass
        else:
            obj.delete()

    def save_related(self, request, form, formsets, change):
        if self.readonly_group(request):
            pass
        else:
            form.save_m2m()
            for formset in formsets:
                self.save_formset(request, form, formset, change=change)
