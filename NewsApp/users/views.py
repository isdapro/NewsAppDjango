from django.shortcuts import render
from eventregistry import *
import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import datetime
from django.utils import timezone
from newsapi import NewsApiClient
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate
from django.contrib.auth import login


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)
