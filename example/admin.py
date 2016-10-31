from django.contrib import admin

from .models import MyModel, MyOtherModel


class MyModelAdmin(admin.ModelAdmin):
    list_display = ('my_first_field', 'my_second_field', 'my_third_field')

admin.site.register(MyModel, MyModelAdmin)


class MyOtherModelAdmin(admin.ModelAdmin):
    fields = ['my_first_field']

admin.site.register(MyOtherModel, MyOtherModelAdmin)
