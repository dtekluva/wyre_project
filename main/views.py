from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from main.models import Reading, Branch
from main.snippets import total_energy, get_reading_stats, js_total_energy, js_get_reading_stats
import json
# import main.fetch_readings

# Create your views here.
# x = Reading.objects.get(id = 1)

# # x.post_datetime = "2019-07-30 16:19:15+00:00"
# x.post_datetime = "2019-07-01T03:45:05.137"

# x.save()



@login_required
def index(request):

        page = "Dashboard"
        user = User.objects.get(pk = request.user.id)
        branches = Branch.objects.filter(user_id = user.id)
        start_date = "2019-07-01"
        end_date = "2019-07-07"

        peak_kw, min_kw, avg_kw = get_reading_stats(user.id, start_date, end_date)
        energy_used = total_energy(user.id, start_date, end_date)

        return render(request, 'dashboard.html', {'user':user, "branches": branches, "page":page, "energy_used" : energy_used, "min_kw": min_kw, "peak_kw": peak_kw, "avg_kw": avg_kw})

def power(request):
        page = "Power Readings (kW)"
        user = User.objects.get(pk = request.user.id)

        return render(request, 'power.html', {'user':user, "page": page})

def voltage(request):
        page = "Voltage Readings (Volts)"
        user = User.objects.get(pk = request.user.id)

        return render(request, 'voltage.html', {'user':user, "page": page})

def current(request):
        page = "Current Readings (Amps)"
        user = User.objects.get(pk = request.user.id)

        return render(request, 'current.html', {'user':user, "page": page})

def interaction(request):
        page = "Interact. (kVAr-kVA-PF)"
        user = User.objects.get(pk = request.user.id)

        return render(request, 'interaction.html', {'user':user, "page": page})

def max_demand(request):
        page = "Max Demand (Amps)"
        user = User.objects.get(pk = request.user.id)

        return render(request, 'max_demand.html', {'user':user, "page": page})

def fetch_vals_period(request):

        user = User.objects.get(pk = request.user.id)
        print(request.POST.get("branch", ""))

        if request.method == "POST":
                start_date = None
                end_date   = None
                
                branches = Branch.objects.filter(user_id = user.id)

        peak_kw, min_kw, avg_kw = get_reading_stats(user.id, start_date, end_date)
        energy_used = total_energy(user.id, start_date, end_date)

        return HttpResponse(json.dumps({"response": "success"}))