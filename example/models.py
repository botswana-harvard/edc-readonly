from django.db import models


class MyModel (models.Model):

    my_first_field = models.CharField(
        verbose_name='How did you break you leg?',
        default=None,
        max_length=50,
        help_text=""
    )

    my_second_field = models.CharField(
        verbose_name='Is this the first time you broke your leg?',
        default=None,
        max_length=50,
        help_text=""
    )

    my_third_field = models.CharField(
        verbose_name='1. When was the last time you where seen by the doctor',
        default=None,
        max_length=50,
        null=True,
        blank=True,
        editable=False,
        help_text=""
    )

    class Meta:
        app_label = 'example'
        verbose_name = "My Model"
        verbose_name_plural = "My Model"


class MyOtherModel (models.Model):

    my_first_field = models.CharField(
        verbose_name='This is just a test field.',
        default=None,
        null=True,
        blank=True,
        max_length=50,
        help_text=""
    )

    my_second_field = models.CharField(
        verbose_name='1. Where do you come from?',
        default=None,
        max_length=50,
        null=True,
        blank=True,
        editable=False,
        help_text=""
    )

    class Meta:
        app_label = 'example'
        verbose_name = "My Other Model"
        verbose_name_plural = "My Other Model"
