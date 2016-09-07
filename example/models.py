from django.db import models


class MyModel (models.Model):

    my_first_field = models.CharField(
        verbose_name='This text was last modified on []',
        default=None,
        null=True,
        blank=True,
        max_length=50,
        help_text=""
    )

    my_second_field = models.CharField(
        verbose_name='The second field text was last modified on [] before the first text was modified.',
        default=None,
        null=True,
        blank=True,
        max_length=50,
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

    class Meta:
        app_label = 'example'
        verbose_name = "My Other Model"
        verbose_name_plural = "My Other Model"
