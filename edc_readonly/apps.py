from django.apps.config import AppConfig as DjangoAppConfig
from edc_base.apps import AppConfig as EdcBaseAppConfigParent
# from edc_protocol.apps import AppConfig as EdcProtocolAppConfigParent


class AppConfig(DjangoAppConfig):
    name = 'edc_readonly'
    model_attrs = None
    institution = 'Botswana Harvard AIDS Institute Partnership'
    project_name = 'EDC Read Only'


class EdcBaseAppConfig(EdcBaseAppConfigParent):
    institution = 'Botswana Harvard AIDS Institute Partnership'
    project_name = 'EDC Read Only'
