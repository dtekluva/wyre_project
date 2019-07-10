from main.models import Reading
import requests
from requests.auth import HTTPBasicAuth
import json



username = "ppl"
password = "Wyre1234"
device_id = "133813"

start_date = "2019-07-07"
end_date = "2019-07-15"

def authenticate(username, password):#LOGIN TO EXPERT POWER PLUS

    req = requests.get(f'http://expertpowerplus.com:8080/api/Login?userName={username}&pass={password}')
    print(req.cookies)
    auth_key_name = (list(req.cookies)[0]).name #get name of cookie unit used to be (.ASPXAUTH) changed to (form_p)
    auth_key_value = dict(req.cookies).get(auth_key_name) #get actual cookie unit

    cookie = {auth_key_name: auth_key_value}

    return cookie

def make_request(cookie, device_id, start_date, end_date):
    
    request = requests.get(f'http://expertpowerplus.com:8080/api/Basic?startDate={start_date}&endDate={end_date}&deviceId={device_id}', cookies=cookie)

    response = request.content
    data = json.loads(response)
    readings = data['data']

    return readings


def populate_db(readings, device):

    
    for record in readings:
        date = record['recordTime'][:10]
        time = record['recordTime'][11:]
        datetime = (record['recordTime']).replace('T'," ")

        reading = record["data"]
        print(reading[0]["value"], record['recordTime'])
        Reading.objects.create(post_date = date, post_time = time, 
                post_datetime = datetime, device_id   =  1,
                user_id = 1,
                voltage_l1_l12 =  reading[0]["value"],
                voltage_l2_l23 = reading[1]["value"], voltage_l3_l31 = reading[2]["value"],
                current_l1     = reading[3]["value"], current_l2     = reading[4]["value"],
                current_l3     = reading[5]["value"],
                kw_l1   = reading[6]["value"], kw_l2   = reading[7]["value"],
                kw_l3   = reading[8]["value"], kvar_l1 = reading[9]["value"],
                kvar_l2 = reading[10]["value"], kvar_l3 = reading[11]["value"],
                kva_l1  = reading[12]["value"], kva_l2  = reading[13]["value"],
                kva_l3  = reading[14]["value"], power_factor_l1  = reading[15]["value"],
                power_factor_l2  = reading[16]["value"], power_factor_l3  = reading[17]["value"],
                total_kw    = reading[18]["value"], total_kvar  = reading[19]["value"],
                total_kva   = reading[20]["value"], total_pf    = reading[21]["value"],
                avg_frequency   = reading[22]["value"], neutral_current = reading[23]["value"],
                kwh_import      = reading[24]["value"], kwh_export      = reading[25]["value"], 
                kvah_total      = reading[26]["value"], max_amp_demand_l1 = reading[27]["value"], max_amp_demand_l2 = reading[28]["value"],
                max_amp_demand_l3 = reading[29]["value"], max_sliding_window_kw_demand   = reading[30]["value"], accum_kw_demand    = reading[31]["value"], max_sliding_window_kva_demand = reading[32]["value"], present_sliding_window_kw_demand    = reading[33]["value"],
                present_sliding_window_kva_demand   = reading[34]["value"]
        )
    
    else: 
        print("Done populating")

def update_user_readings(user_id):
        last_update = (Reading.objects.filter(user_id = user_id).order_by("-id")[0]).post_datetime
        

cookies = authenticate(username,password)
readings = make_request(cookies, device_id, start_date, end_date)
populate_db(readings, 1)