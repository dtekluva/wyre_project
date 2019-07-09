from main.models import Reading, Customer, Location, Reading, Device
import requests
from requests.auth import HTTPBasicAuth
import json

def get_readings(device_id, start_date, end_date, target):
    start_date = "2019-07-01"
    end_date = "2019-07-07"

    readings = Reading.objects.filter(device__id = device_id, post_datetime__range = (start_date, end_date)).values_list(target)
 
    return readings

def get_device_reading_for_period(start_date, end_date, device_id):
    start_date = "2019-07-01"
    end_date = "2019-07-07"

    readings = Reading.objects.filter(device__id = device_id, post_datetime__range = (start_date, end_date)).values_list('kwh_import')

    if len(readings) != 0:

        total_kwh_device  = readings[0][0] - readings[len(readings)-1][0]
    
    else:

        return 0

    return total_kwh_device

def total_energy(user_id, start_date, end_date):
    
    devices = Device.objects.filter(user__id = user_id)

    reading_collections = map(lambda x: get_device_reading_for_period(start_date, end_date, x.id), devices)
    total_kwh = sum(list(reading_collections))

    return total_kwh

def get_reading_stats(user_id, start_date, end_date):

    devices = Device.objects.filter(user__id = user_id)
    target = "total_kw"
    readings = []
    for device in devices:

        readings += [x[0] for x in  list(get_readings(device.id, start_date, end_date, target))]#UNWRAP TUPLES AND REMOVE INTEGER VALUES
    
    max_read = int(max(readings))
    min_read = int(min(readings))
    avg_read = int(sum(readings)/len(readings))

    return max_read, min_read, avg_read

###########################################################################
####################                                    ###################
##################  JAVASCRIPT FILTER BY BRANCH AND TIME  #################
####################                                    ###################
###########################################################################

def js_get_readings(device_id, start_date, end_date, target):
    start_date = "2019-07-01"
    end_date = "2019-07-07"

    readings = Reading.objects.filter(device__id = device_id, post_datetime__range = (start_date, end_date)).values_list(target)
 
    return readings

def js_get_device_reading_for_period(start_date, end_date, device_id):
    start_date = "2019-07-01"
    end_date = "2019-07-07"

    readings = Reading.objects.filter(device__id = device_id, post_datetime__range = (start_date, end_date)).values_list('kwh_import')

    if len(readings) != 0:

        total_kwh_device  = readings[0][0] - readings[len(readings)-1][0]
    
    else:

        return 0

    return total_kwh_device

def js_total_energy(user_id, start_date, end_date):
    
    devices = Device.objects.filter(user__id = user_id)

    reading_collections = map(lambda x: js_get_device_reading_for_period(start_date, end_date, x.id), devices)
    total_kwh = sum(list(reading_collections))

    return total_kwh

def js_get_reading_stats(user_id, start_date, end_date):

    devices = Device.objects.filter(user__id = user_id)
    target = "total_kw"
    readings = []
    for device in devices:

        readings += [x[0] for x in  list(js_get_readings(device.id, start_date, end_date, target))]#UNWRAP TUPLES AND REMOVE INTEGER VALUES
    
    max_read = int(max(readings))
    min_read = int(min(readings))
    avg_read = int(sum(readings)/len(readings))

    return max_read, min_read, avg_read