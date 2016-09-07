from django.apps import apps as django_apps


class ReadOnlyAdminMixin:
    """Disables all editing capabilities."""

    def get_readonly_fields(self, request, obj=None):
        app_config = django_apps.get_app_config('edc_readonly_admin')
        self.readonly_auth_group = app_config.readonly_auth_group_name
        readonly_fields = []
        groups = [x.name for x in request.user.groups.all()]
        if self.readonly_auth_group in groups:
            for field in self.get_fields(request, obj):
                readonly_fields.append(field)
        return list(set(readonly_fields))

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass

    def delete_model(self, request, obj):
        pass

    def save_related(self, request, form, formsets, change):
        pass
