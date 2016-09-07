from django.apps.config import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'edc_readonly_admin'
    model_attrs = None
    readonly_auth_group_name = 'Monitors'
