from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings
from main.models import  * # Reading, Branch, Device, Customer, Document
from main.helpers.snippets import total_energy, get_reading_stats, js_total_energy, js_get_reading_stats, format_date, js_get_readings, get_energy_usage
from main.helpers.datalogs import utility_vs_gen, daily_utility_vs_gen_kwh, get_last_readings
import json, datetime, calendar
from django.core.serializers.json import DjangoJSONEncoder
from main.helpers.fetch_readings import run_migrations
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# x = Reading.objects.get(id = 1)
# Reading.objects.all().delete()
# # x.post_datetime = "2019-07-30 16:19:15+00:00"
# x.post_datetime = "2019-07-01T03:45:05.137"
# x.save()
cache = {}

def get_date_range():
        today = datetime.datetime.now()
        today_year = today.year
        today_month = today.month
        month_last_day = calendar.monthrange(today_year, today_month)[1]

        default_start_date = f"{today_year}-{today_month}-01"
        default_end_date = f"{today_year}-{today_month}-{month_last_day}"

        return default_start_date, default_end_date

def get_raw_range_for_js(add_one_day = False):
        if not add_one_day:
                today = datetime.datetime.now()
                today_year = today.year
                today_month = today.month
                month_last_day = calendar.monthrange(today_year, today_month)[1]

                default_start_date = f"{today_month}/01/{today_year}"
                default_end_date = f"{today_month}/{month_last_day}/{today_year}"

        if add_one_day:
                today = datetime.datetime.now()
                tommorrow = datetime.datetime.now() + datetime.timedelta(days = 1)
                today_year, today_month, today_day= today.year, today.month, today.day
                tommorrow_year, tommorrow_day, tommorrow_month = tommorrow.year, tommorrow.day, tommorrow.month

                default_start_date = f"{today_month}/{today_day}/{today_year}"
                default_end_date = f"{tommorrow_month}/{tommorrow.day}/{tommorrow_year}"

        return default_start_date, default_end_date

@login_required
def index(request):
        default_start_date, default_end_date = get_raw_range_for_js()

        page = "Dashboard"
        user = User.objects.get(pk = request.user.id)
        customer = Customer.objects.get(user = user)
        branches = Branch.objects.filter(user_id = user.id)
        devices = Device.objects.filter(user_id = request.user.id)
        start_date, end_date = get_date_range()

        peak_kw, min_kw, avg_kw = "--", "--", "--" #get_reading_stats(user.id, start_date, end_date)
        energy_used = "loading.."#total_energy(user.id, default_start_date, default_end_date)

        return render(request, 'dashboard.html', {'user':user, "customer": customer, "branches": branches,"devices": devices, "page":page, "energy_used" : energy_used, "min_kw": min_kw, "peak_kw": peak_kw, "avg_kw": avg_kw, "def_start_date":default_start_date, "def_end_date":default_end_date})

def power(request):
        page = "Power Readings (kW)"
        user = User.objects.get(pk = request.user.id)
        customer = Customer.objects.get(user = user)
        branches = Branch.objects.filter(user_id = user.id)
        devices = Device.objects.filter(user_id = request.user.id)

        return render(request, 'power.html', {'user':user, "customer": customer, "page": page, "devices":devices})
@login_required
def last_read(request):
        
        page = "Last Readings"
        user = User.objects.get(pk = request.user.id)
        customer = Customer.objects.get(user = user)
        branches = Branch.objects.filter(user_id = user.id)
        devices = Device.objects.filter(user_id = request.user.id)

        return render(request, 'last_read.html', {'user':user, "customer": customer, "page": page, "devices":devices})

def voltage(request):
        page = "Voltage Readings (Volts)"
        user = User.objects.get(pk = request.user.id)
        customer = Customer.objects.get(user = user)

        return render(request, 'voltage.html', {'user':user, "customer": customer, "page": page})

def current(request):
        page = "Current Readings (Amps)"
        user = User.objects.get(pk = request.user.id)
        customer = Customer.objects.get(user = user)

        return render(request, 'current.html', {'user':user, "customer": customer, "page": page})

@login_required
def readings(request):
        page = "Readings"
        user = User.objects.get(pk = request.user.id)
        customer = Customer.objects.get(user = user)
        devices = Device.objects.filter(user_id = request.user.id)
        start_date, end_date = get_raw_range_for_js(add_one_day=True)
        parameters = ["Current (Amps)", "Voltage (Volts)", "Active-Power (kW)", "Reactive-Power (kvar)", "Energy (kWH)"]

        return render(request, 'readings.html', {'user':user, "customer": customer, "page": page, "devices":devices, "parameters":parameters, "def_start_date":start_date, "def_end_date":end_date})

def max_demand(request):
        page = "Max Demand (Amps)"
        user = User.objects.get(pk = request.user.id)
        customer = Customer.objects.get(user = user)    
        return render(request, 'max_demand.html', {'user':user, "customer": customer, "page": page})

def score_card(request):
        page = "Score Card"
        user = User.objects.get(pk = request.user.id)
        customer = Customer.objects.get(user = user)

        device_id = request.POST.get("device", "")
        devices = Device.objects.filter(user__id = user.id) if device_id == "None" else Device.objects.filter(user = user)


        return render(request, 'score_card.html', {'user':user, "customer": customer, "page": page, "devices": devices})

@login_required
def messaging(request):

        page = "Messaging"
        user = User.objects.get(pk = request.user.id)

        customer = Customer.objects.get(user = user)
        customer.get_messages()
        conversation_partners = customer.get_conversation_partners()
        # print(conversation_partners)
        
        device_id = request.POST.get("device", "")
        devices = Device.objects.filter(user__id = user.id) if device_id == "None" else Device.objects.filter(user = user)

        return render(request, 'messaging.html', {'user':user, "customer": customer, "page": page, "devices": devices, "conversation_partners": conversation_partners})



###########################################################
###########################################################
#APISs SECTION
@login_required
def fetch_messages(request):
        user = User.objects.get(pk = request.user.id)
        
        customer = Customer.objects.get(user = user)
        messages = customer.get_messages()
        

        return HttpResponse(json.dumps({"response": "success", "data": messages}))

def send_message(request):
        user = User.objects.get(pk = request.user.id)
        

        if request.method == "POST":
                # print("REQUEST IS POST !!!")

                customer = Customer.objects.get(user = user)
                messages = customer.get_messages()
                data = json.loads(request.body)
                receiver = Customer.objects.get(id = data["customer_id"])
                text = data["text"]
                title = "no title"

                Message(sender = customer, receiver = receiver, description = title, content = text ).save()

                return HttpResponse(json.dumps({"response": "success", "data": messages}))

@login_required
def check_new_message(request):
        user = User.objects.get(pk = request.user.id)
        

        if request.method == "POST":
                # print("REQUEST IS POST !!!")

                customer = Customer.objects.get(user = user)
                conversation_partners = customer.get_conversation_partners()

                # print(conversation_partners)

        



def fetch_vals_period(request):
        #THIS IS SIMILAR TO THE (fetch_vals_period_per_device) FUNCTION ONLY THAT THIS FUNCTION ONLY FETCHES FOR ALL THE DEVICES I.E GETS OVERALL TOTAL FOR ALL DEVICES OF A CUSTOMER

        user = User.objects.get(pk = request.user.id)
        
        if request.method == "POST":

                branch_id = request.POST.get("device", "")
                devices = Device.objects.filter(user_id = request.user.id)
                start_date, end_date = request.POST.get("period", "").split("-")#SPLIT VALUES TO INDIVIDUAL DATES
                #####REPLACE SLASHES WITH DASHES######
                start_date = format_date(start_date.replace("/","-"))
                end_date = format_date(end_date.replace("/","-"))

                user_cache = cache.get(user, False)

                if user_cache and  (datetime.datetime.now() - user_cache["lastlog"]).seconds < settings.CACHE_EXPIRY:
                        data = user_cache["data"]
                else:

                        peak_kw, min_kw, avg_kw = js_get_reading_stats(user.id, start_date, end_date)
                        energy_used = js_total_energy(user.id, start_date, end_date)
                        
                        utility_times, gen1_times, gen2_times = utility_vs_gen(devices, start_date, end_date)
                        
                        devices = Device.objects.filter(user_id = request.user.id)
                        
                        daily_device_usage = daily_utility_vs_gen_kwh(devices, start_date, end_date)

                        data = {"peak_kw": peak_kw, "min_kw": min_kw, "avg_kw":avg_kw, "energy_used": energy_used, "gen1_times":gen1_times,"gen2_times":gen2_times, "utility_times":utility_times, "daily_device_usage":daily_device_usage}

                        cache[user] = {"lastlog":datetime.datetime.now(), "data":data}

        return HttpResponse(json.dumps({"response": "success", "data": data}))


def fetch_vals_period_per_device(request):
        #THIS IS SIMILAR TO THE (fetch_vals_period) FUNCTION ONLY THAT THIS FUNCTION ONLY FETCHES FOR ALL THE DEVICES I.E GETS VALUE FOR JUST ONE DEVICE OF A CUSTOMER ALTHOUGH IT STILL HAS THE ABILITY TO FETCH OVERALL TOTAL.

        user = User.objects.get(pk = request.user.id)

        if request.method == "POST":

                device_id = request.POST.get("device", "")
                devices = Device.objects.filter(id = device_id)
                start_date, end_date = request.POST.get("period", "").split("-")#SPLIT VALUES TO INDIVIDUAL DATES
                #####REPLACE SLASHES WITH DASHES######
                start_date = format_date(start_date.replace("/","-"))
                end_date = format_date(end_date.replace("/","-"))

        try:
                peak_kw, min_kw, avg_kw = js_get_reading_stats(user.id, start_date, end_date, device_id = device_id)
                energy_used = js_total_energy(user.id, start_date, end_date, device_id = device_id)
                
                utility_times, gen1_times, gen2_times = utility_vs_gen(devices, start_date, end_date)

                daily_device_usage = daily_utility_vs_gen_kwh(devices, start_date, end_date)                

                return HttpResponse(json.dumps({"response": "success", "data": {"peak_kw": peak_kw, "min_kw": min_kw, "avg_kw":avg_kw, "energy_used": energy_used, "gen1_times":gen1_times,"gen2_times":gen2_times, "utility_times":utility_times, "daily_device_usage" : daily_device_usage}}))
        
        except:
                return HttpResponse(json.dumps({"response": "failure"}))
        
def get_last_read(request):

        user = User.objects.get(pk = request.user.id)

        if request.method == "POST":

                device = request.POST.get("device", "")
                device_id = Device.objects.get(id = device)
                
                last_read = get_last_readings(device_id = device_id)

                return HttpResponse(json.dumps({"response": "success", "data":last_read}))



##THIS FUNCTION GETS THE MINIMUM AND MAXIMUM VALUES FOR ALL DEVICES TO BE SHOWN ON THE BARGRAPH 

def get_min_max_each_device(devices, start_date, end_date):
        
        result = {"devices":[],"max_reads":[], "min_reads":[]}

        for device in devices:

                readings = []

                readings = [x[0] for x in  list(js_get_readings(device.id, start_date, end_date, "total_kw")) if x[0] > 0]#UNWRAP TUPLES AND REMOVE INTEGER VALUES

                if len(readings) > 0:
                        max_read = int(max(readings))
                        min_read = int(min(readings))
                else:
                        min_read = max_read = avg_read = 0


                result["devices"].append(device.name)
                result["max_reads"].append(max_read)
                result["min_reads"].append(min_read)
        
        return result

def get_line_readings(request): 

        user = User.objects.get(pk = request.user.id)

        if request.method == "POST":

                device_id = request.POST.get("device", "")
                devices = Device.objects.filter(id = device_id)
                date = request.POST.get("date", "")
                #####REPLACE SLASHES WITH DASHES######
                date = format_date(date.replace("/","-"))

                end_date = date + datetime.timedelta(days = 1) #ADD ONE DAY TO DAY TO ENABLE FILTERING BY DURATION AS YOU CANNOT FILTER BY ONE DAY.

                raw_data = list(Reading.objects.filter(device__id = device_id, post_datetime__range = (date, end_date)).defer('post_datetime','post_date').order_by('post_datetime').values())

                data = raw_data # map(lambda __date: __date.strftime("%I:%M %p"))


        try:
                return HttpResponse(json.dumps({"response": "success", "data": data}, sort_keys=True, indent=1, cls=DjangoJSONEncoder))
        except:
                return HttpResponse(json.dumps({"response": "failure"}))

def get_line_readings_log(request): #READINGS FOR LINE CHARTS IN READINGS PAGE
        #THIS IS SIMILAR TO THE (get_line_readings) FUNCTION ONLY THAT THIS FUNCTION ONLY FETCHES FOR LOG TABLE

        user = User.objects.get(pk = request.user.id)

        if request.method == "POST":
                device_id = request.POST.get("device", "")
                devices = Device.objects.filter(id = device_id)
                date, end_date = request.POST.get("period", "").split("-") 

                #####REPLACE SLASHES WITH DASHES######
                date = format_date(date.replace("/","-"))
                end_date = format_date(end_date.replace("/","-"))

                raw_data = list(Reading.objects.filter(device__id = device_id, post_datetime__range = (date, end_date)).defer('post_datetime','post_date').order_by('post_datetime').values())

                data = raw_data # map(lambda __date: __date.strftime("%I:%M %p"))
                # # print(data)
                for i in range(len(data)):
                        data[i]["post_datetime"] = data[i]["post_datetime"].strftime("%b. %d, %Y, %I:%M %p.")

        try:
                return HttpResponse(json.dumps({"response": "success", "data": data}, sort_keys=True, indent=1, cls=DjangoJSONEncoder))
        except:
                return HttpResponse(json.dumps({"response": "failure"}))

def get_yesterday_today_usage(request):
        user = User.objects.get(pk = request.user.id)
        device_id = request.POST.get("device", "None")
        devices = Device.objects.filter(user__id = user.id) if device_id == "None" else Device.objects.filter(id = device_id)
        # # print(devices)
        
        today_energy, yesterday_energy = get_energy_usage(devices)


        return HttpResponse(json.dumps({"response": "success", "data":{"today_energy":today_energy, "yesterday_energy": yesterday_energy}}, sort_keys=True, indent=1, cls=DjangoJSONEncoder))

def get_capacity_factors(request):
        user = User.objects.get(pk = request.user.id)
        device_id = request.POST.get("device", "None")
        
        branches = user.branch_user.all()
        response = {}

        for branch in branches:

                devices = branch.device_branch.all()

                if not response.get(branch.name, False): 
                        response[branch.name] = {}

                for device in devices:
                        response[device.name] = {
                                "capacity_factor": device.get_capacity_factor(),
                                "facility_energy_load_factor": device.get_facility_energy_load_factor(),
                                "baseline" : device.base_line_energy()
                        }

                        # file = open(f"{device.device_id}_MONTHLY.py", "w")
                #         # baseline = device.base_line_energy()
                #         # print(device.name)
                # # print(response)
                                

        return HttpResponse(json.dumps({"response": "success", "data":{"base_line":response}}, sort_keys=True, indent=1, cls=DjangoJSONEncoder))


#URL FOR POPULATING DATABASE
def load_readings(request):
        Datalog().populate()
        run_migrations()

        try:

                return HttpResponse(json.dumps({"response": "success"}))
                        
        except:
                return HttpResponse(json.dumps({"response": "failure", "message": "Something went wrong"}))


###########################################################
###########################################################
############## LOAD NEW CDD ###############################
@csrf_exempt
def upload_cdd(request):

        if request.method == 'POST':
                file = request.FILES.get("file")
                data = file.readlines()
                
                Degree_Day.add_values(data)

                return HttpResponse(json.dumps({"response": "success", "message": f"added {len(data)} new cdds'"}))
        else:
                        return HttpResponse(json.dumps({"response": "error", "message": "Bad request"}))

def simple_upload(request):

        # # print(type(request.FILES.get("file")))
        file = request.FILES.get("file")
        doc = Document(document = file)
        doc.save()
        if request.method == 'POST':
                # # print(request.POST)
                return HttpResponse(json.dumps({"response": "success", "message": doc.document.url}))
                
        return render(request, 'upload.html')