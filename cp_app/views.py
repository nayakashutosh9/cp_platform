from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import DetailView
from . import models
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.forms import formset_factory
import random
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
# Create your views here.
def index(request):
    return render(request, 'index.html')
def register(request):
    return render(request,'register.html')
def discuss(request):
    return render(request,'discuss.html')
def home(request):
    return render(request,'home.html')
def user_login(request):
    return render(request,'login.html')
