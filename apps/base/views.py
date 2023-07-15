import re

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render


# Create your views here.
def register(request):
    if request.method == 'POST':
        print('###########################################')
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        username_regex = r'^\+998\d{2}\d{3}\d{2}\d{2}$'
        username_regex2 = r'^\+998\d{2}\d{3}\d{2}\d{2}$'
        username_regex3 = r'^\d{2}\d{3}\d{2}\d{2}$'

        if not re.match(username_regex, username):
            if not re.match(username_regex2, username):
                if not re.match(username_regex3, username):
                    messages.warning(request, "Invalid phone number! The phone number must be +998994187100 characters!")
                    return redirect('register')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.warning(request, "User already exists!")
            return redirect('register')
        else:
            if password1 == password2:
                instance = User.objects.create_user(username=username, password=password1)
                user = authenticate(username=username, password=password1)
                if user is not None:
                    login(request, user)
                messages.success(request, 'Your account has been created!')
                return redirect('/')
            else:
                messages.warning(request, "Passwords do not match")
                return redirect('register')
    return render(request, "register.html")


def login_func(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Error !! Phone number or Password is incorrect")
            return HttpResponseRedirect('/login')

    return render(request, "login.html")


def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')


from urllib.parse import urlparse

from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        # try:
        view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        # except Resolver404:
        #     view = None
        # if view:
        #     break

    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response


def selectlanguage(request):
    if request.method == 'POST':  # check post
        cur_language = translation.get_language()
        lasturl = request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY] = lang
        # return HttpResponse(lang)
        return HttpResponseRedirect("/" + lang)
