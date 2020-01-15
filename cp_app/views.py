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
from cp_app.models import UserProfileInfo,Problem,Tag
from cp_app.forms import UserForm, UserProfileInfoForm,SearchForm
import random
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
# Create your views here.
@login_required
def index(request):
    form = SearchForm()
    q2 = Tag.objects.all()
    q1 = Problem.objects.none()
    if request.method == "POST":
        form = SearchForm(data=request.POST or None )
        if form.is_valid():
            print("BYE")
            tag_query=form.cleaned_data['tag']
            print(tag_query)
            q1 = Problem.objects.filter(tag__name__iexact=tag_query)
            if q1:
                    return render(request,'index.html',{'form':form, 'problems':q1, "tags":q2})
            else:
                print("fuck")
    else:
        q1 = Problem.objects.all()
    print('hi')
    return render(request,'index.html',{'form':form, 'problems':q1,'tags':q2})
def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print("ERROR")
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'register.html',{'registered':registered,'user_form':user_form,'profile_form':profile_form})
def discuss(request):
    return render(request,'discuss.html')
def home(request):
    return render(request,'home.html')
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    return HttpResponse("ACCOUNT NOT ACTIVE")
            else:
                messages.error(request,'Username or Password not correct! Try Again!')
                return render(request, 'login.html',{})
        else:
            return render(request, 'login.html',{})
    else:
        return HttpResponseRedirect(reverse('home'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('cp_app:user_login'))
