class ReadOnlyAdminMixin:
    """Disables all editing capabilities."""

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = []
        for field in self.get_fields(request, obj):
            readonly_fields.append(field)
        print(readonly_fields)
        return readonly_fields

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
