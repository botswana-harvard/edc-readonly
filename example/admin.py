from django.contrib import admin

from edc_readonly_admin.readonly_admin_mixin import ReadOnlyAdminMixin

from .models import MyModel, MyOtherModel


class MyModelAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    fields = ['my_first_field', 'my_second_field', 'my_third_field']
    readonly_fields = ['my_third_field']
    readonly = ['my_third_field']
    list_display = ('my_first_field', 'my_second_field', 'my_third_field')

admin.site.register(MyModel, MyModelAdmin)


class MyOtherModelAdmin(admin.ModelAdmin):
    fields = ['my_first_field']
    readonly_fields = ['my_second_field']

admin.site.register(MyOtherModel, MyOtherModelAdmin)
