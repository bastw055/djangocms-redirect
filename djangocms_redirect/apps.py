from django.apps import AppConfig

# an app config that simulates the native django.contrib.redirects app name
class ContribConfig(AppConfig):
    name = 'djangocms_redirect'
    verbose_name = 'Redirects'