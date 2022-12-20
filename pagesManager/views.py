from datetime import datetime

from pagesManager.models import Profile

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import activate
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def active_lang(request):
    if request.session.get('lang') is not None:
        activate(request.session['lang'])
    else:
        request.session['lang'] = 'en'
        activate("en")


def set_lang_en_func(request):
    request.session['lang'] = 'en'
    activate("en")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def set_lang_es_func(request):
    request.session['lang'] = 'es'
    activate("es")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def login_func(request):
    if check_authenticate(request):
        return redirect('/home_view/')
    username = request.POST.get('userName')
    password = request.POST.get('inputPassword')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        request.session['login'] = True
        profile = Profile.objects.get(user_name=request.user)
        now = datetime.now()
        request.session['level'] = profile.key_id
        request.session['tab'] = "Home"
        request.session['last_login'] = now.strftime('%y%m%d-%H%M%S')
        profile.last_login = request.session['last_login']
        request.session['Result'] = ''
        request.session['CusName'] = ''
            
        profile.save()
        messages.success(request, 'Wellcome '+ username)
        return redirect('/home_view/')
    else:
        messages.error(request, 'error')
        print('error')
        return redirect('/login_view/')


def logout_func(request):
    logout(request)
    request.session['login'] = False
    request.session.clear()
    return redirect('/login_view/')


def login_view(request):
    if not check_authenticate(request):
        return render(request, 'login_view.html')
    return render(request, 'home_view.html')


def home_view(request):
    if not check_authenticate(request):
        return redirect('/login_view/')
    #print(request.session['level'])
    pageTitle = "Home"
    context = {'pageTitle': pageTitle,}
    if request.session['level'] == 2:
        return redirect('/yogurt_checkIn/')
    else:
        return render(request, 'home_view.html', context)


def change_pass_func(request):
    if not check_authenticate(request):
        return redirect('/login_view/')
    username = request.user
    passwordOld = request.POST.get('inputPasswordOld')
    PasswordNew = request.POST.get('inputPasswordNew')
    PasswordNewVerify = request.POST.get('inputPasswordNewVerify')
    userNow = authenticate(username=username, password=passwordOld)
    if userNow is not None and PasswordNew == PasswordNewVerify:
        userNow.set_password(PasswordNew)
        userNow.save()
        logout(request)
        request.session.clear()
        login(request, userNow)
        request.session['login'] = True
        profile = Profile.objects.get(user_name=request.user)
        now = datetime.now()
        request.session['level'] = profile.key_id
        request.session['location'] = profile.location
        request.session['last_login'] = now.strftime('%y%m%d-%H%M%S')
        profile.last_login = request.session['last_login']
        profile.save()
        print('Pass change')
        messages.success(request, 'Pass change')
    else:
        messages.warning(request, 'Pass wrong')
        print('Pass wrong')
    return redirect('/home_view/')


def check_authenticate(request):
    active_lang(request)
    if request.session.get('login') is not None:
        profile = Profile.objects.get(user_name=request.user)
        if request.session['last_login'] != profile.last_login:
            logout_func(request)
            return False
        return request.session['login']
    else:
        return False


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'error_404.html', data)

