import django
from main.models import *
from helpers.fetch_readings import run_migrations
import time

run_migrations()
Datalog().populate()
Device.populate_previous_scores