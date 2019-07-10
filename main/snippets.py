from main.models import Reading, Customer, Location, Reading, Device
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import json

def get_readings(device_id, start_date, end_date, target):
    start_date = "2019-07-01"
    end_date = "2019-07-30"

    readings = Reading.objects.filter(device__id = device_id, post_datetime__range = (start_date, end_date)).values_list(target)
 
    return readings

def get_device_reading_for_period(start_date, end_date, device_id):
    start_date = "2019-07-01"
    end_date = "2019-07-30"

    readings = Reading.objects.filter(device__id = device_id, post_datetime__range = (start_date, end_date)).order_by("post_datetime").values_list('kwh_import')

    if len(readings) != 0:

        total_kwh_device  = readings[len(readings)-1][0] - readings[0][0]
    
    else:

        return 0

    return total_kwh_device

def total_energy(user_id, start_date, end_date):#GETS THE ENERGY DIFFERENCE FROM A START DATE TO END DATE FOR A ALL DEVICES IN ALL LOCATIONS FOR A USER
    
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
    
    if len(readings) > 0:
        max_read = int(max(readings))
        min_read = int(min(readings))
        avg_read = int(sum(readings)/len(readings))
    else:
        min_read = max_read = avg_read = 0

    return max_read, min_read, avg_read

###########################################################################
####################                                    ###################
##################  JAVASCRIPT FILTER BY BRANCH AND TIME  #################
####################                                    ###################
###########################################################################

def js_get_readings(device_id, start_date, end_date, target):

    readings = Reading.objects.filter(device__id = device_id, post_datetime__range = (start_date, end_date)).values_list(target)
 
    return readings

def js_get_device_reading_for_period(start_date, end_date, device_id):

    readings = Reading.objects.filter(device__id = device_id, post_datetime__range = (start_date, end_date)).order_by("post_datetime").values_list('kwh_import')

    if len(readings) != 0:

        total_kwh_device  = readings[len(readings)-1][0] - readings[0][0]
    
    else:

        return 0

    return total_kwh_device

def js_total_energy(user_id, branch_id, start_date, end_date):
    
    devices = Device.objects.filter(branch_id = branch_id)

    reading_collections = map(lambda x: js_get_device_reading_for_period(start_date, end_date, x.id), devices)
    total_kwh = sum(list(reading_collections))

    return total_kwh

def js_get_reading_stats(user_id, branch_id, start_date, end_date):

    target = "total_kw"
    readings = []

    devices = Device.objects.filter(branch_id = branch_id)

    for device in devices:

        readings += [x[0] for x in  list(js_get_readings(device.id, start_date, end_date, target))]#UNWRAP TUPLES AND REMOVE INTEGER VALUES
    print(readings)
    if len(readings) > 0:
        max_read = int(max(readings))
        min_read = int(min(readings))
        avg_read = int(sum(readings)/len(readings))
    else:
        min_read = max_read = avg_read = 0


    return max_read, min_read, avg_read

def format_date(date):###THIS FUNCTION CONVERTS DATE FROM DD-MM-YYY TO YYY-MM-DD

    month, day, year = date.split("-")
    formatted_date = f"{year.strip()}-{month.strip()}-{day.strip()}"
    datetime_object = datetime.strptime(formatted_date, '%Y-%m-%d')

    return datetime_object