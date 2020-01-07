from django.core.management.base import BaseCommand
from main.models import *
from main.helpers.fetch_readings import run_migrations


try:

    run_migrations()
except:
    pass

# def update_historic_scores(request):

#         devices = Device.objects.all()                        

#         for device in devices:
#                 device.populate_previous_scores()
