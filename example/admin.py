from django.contrib import admin

from edc_readonly_admin.readonly_admin_mixin import ReadOnlyAdminMixin

from .models import MyModel, MyOtherModel


class MyModelAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    fields = ['my_first_field', 'my_second_field']

admin.site.register(MyModel, MyModelAdmin)


class MyOtherModelAdmin(admin.ModelAdmin):
    fields = ['my_first_field']

admin.site.register(MyOtherModel, MyOtherModelAdmin)
