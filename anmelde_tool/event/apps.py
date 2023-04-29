from django.apps import AppConfig
from django.db.models.signals import pre_delete, post_save


class EventConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'anmelde_tool.event'

    def ready(self):
        from anmelde_tool.event import signals as event_signals
        from anmelde_tool.event import models as event_models
        # pre_delete.connect(event_signals.pre_delete_registration, sender=event_models.Registration,
        #                    dispatch_uid="pre_delete_registration")
        post_save.connect(event_signals.post_save_registation, sender=event_models.Registration,
                          dispatch_uid="post_save_registration")
