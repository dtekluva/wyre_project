from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from useraccounts.forms import LoginForm
from django.contrib.auth.models import User
# from useraccounts.models import UserAccount, Token_man, Session
# from main.models import Farmland, Herdsman
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
# from snippet import helpers
import ast


def login_view(request):

        if request.method == 'POST':
                # form = LoginForm(request.POST)

                if True:

                        email    = request.POST.get("email", "")
                        username = request.POST.get("username", "")
                        email = email.lower()
                        password    = request.POST.get("password", "")

                        try:
                                #GET CORRESPONDING USERNAME FROM EMAIL POSTED
                                # username = User.objects.get(email = email).username
                                user = authenticate(username = username.lower(), password = password)

                                user = User.objects.get(username=username)
                                if (user.username == username): #allows user to login using username
                                        # No backend authenticated the credentials

                                        user = User.objects.get(username=username)
                                        login(request, user)

                                        return HttpResponse(json.dumps({"response":"success"}))
                        except:
                                return HttpResponse(json.dumps({"response":"failure"}))    
                                # return render(request, 'resolute/registration/login.html', {'form' : form, 'error':'Sorry incorrect Username or Password !!!'})

        else:
                return render(request, "login.html")