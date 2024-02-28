from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from twilio.rest import Client
from sms_send.models import SMS
from django.contrib.auth.decorators import login_required
from userapp.forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

#from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

@login_required
def home(request):
    context ={
        'smss': SMS.objects.filter(author=request.user)
        }
    return render(request, 'home.html', context)