from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.

@login_required
def index(request):
        page = "Dashboard"
        user = User.objects.get(pk = request.user.id)
        # page = 'user'
        # users =  User.objects.filter(is_staff = True)
        # person = User.objects.get(id = 1)
        # print(person.useraccount.phone)
        # print(users)
        return render(request, 'dashboard.html', {'user':user, "page":page})

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