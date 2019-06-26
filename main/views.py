from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
        # page = 'user'
        # users =  User.objects.filter(is_staff = True)
        # person = User.objects.get(id = 1)
        # print(person.useraccount.phone)
        # print(users)
        return render(request, 'dashboard.html') #{'page':page,'users':users})