from django.apps import AppConfig
from django.db.models import BigAutoField

class CaloriesConfig(AppConfig):
    name = 'calories'

    def ready(self):
    	import calories.signals

default_auto_field = BigAutoField
