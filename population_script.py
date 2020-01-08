# import django
# from main.models import *
# from helpers.fetch_readings import run_migrations
# import time

# run_migrations()
# Datalog().populate()
# Device.populate_previous_scores

def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)

implicit()