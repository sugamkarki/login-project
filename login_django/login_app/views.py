from django.shortcuts import render
from login_app.forms import UserForm, UserProfileInfoForm
from django.urls import reverse 
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect, HttpResponse 
from django.contrib.auth import login, logout, authenticate

def index(request):
    context = {
    }
    return render(request, 'login_app/index.html', context )



def registration(request):
    registered = False 
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = { 
        'user_form':user_form,
        'profile_form':profile_form,
        'registered':registered,
    }

    return render(request, 'login_app/registration.html', context)

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account is not active')
        else:
            print('someone tried to login and failed ')
            return HttpResponse('Invalid login details')
    else:
        return render(request, 'login_app/login.html', {})

def user_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('index'))



        
