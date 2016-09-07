from django import forms

from .models import MyModel, MyOtherModel


class MyModelForm (forms.ModelForm):

    class Meta:
        model = MyModel
        fields = '__all__'


class MyOtherModelForm (forms.ModelForm):

    class Meta:
        model = MyOtherModel
        fields = '__all__'
