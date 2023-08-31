import re
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

from apps.base.forms import ResumeForm
from apps.base.models import UserType, Resume
from apps.product.models import Category
from urllib.parse import urlparse

from django.conf import settings
from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation


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
                    messages.warning(request,
                                     "Invalid phone number! The phone number must be +998994187100 characters!")
                    return redirect('register')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.warning(request, "User already exists!")
            return redirect('register')
        else:
            if password1 == password2:
                instance = User.objects.create_user(username=username, password=password1)
                role = UserType.objects.create(user=instance)
                user = authenticate(username=username, password=password1)
                if user is not None:
                    login(request, user)
                messages.success(request, 'Your users has been created!')
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


# def set_language(request, language):
#     for lang, _ in settings.LANGUAGES:
#         translation.activate(lang)
#         # try:
#         view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
#         # except Resolver404:
#         #     view = None
#         # if view:
#         #     break
#
#         if view:
#             translation.activate(language)
#             next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
#             response = HttpResponseRedirect(next_url)
#             response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
#         else:
#             response = HttpResponseRedirect("/")
#         return response


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        view = resolve(request.META.get("HTTP_REFERER"))
        if view:
            translation.activate(language)
            next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
            response = HttpResponseRedirect(next_url)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
            return response
    return HttpResponseRedirect("/")


# def selectlanguage(request):
#     if request.method == 'POST':  # check post
#         cur_language = translation.get_language()
#         lasturl = request.META.get('HTTP_REFERER')
#         lang = request.POST['language']
#         translation.activate(lang)
#         request.session[translation.LANGUAGE_SESSION_KEY] = lang
#         # return HttpResponse(lang)
#         return HttpResponseRedirect("/" + lang)

def selectlanguage(request):
    if request.method == 'POST':
        cur_language = translation.get_language()
        last_url = request.META.get('HTTP_REFERER')
        lang = request.POST.get('language')
        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY] = lang
        return HttpResponseRedirect(f"/{lang}")


def resume_create(request):
    if not request.user.is_authenticated:
        return redirect('register')

    resume = Resume.objects.filter(user_id=request.user.id).first()
    form = ResumeForm(instance=resume)

    if request.method == "POST":
        inst = Resume.objects.filter(user_id=request.user.id).first()
        if inst:
            form = ResumeForm(request.POST, request.FILES or None, instance=inst)
            if form.is_valid():
                github = form.cleaned_data['github']
                linkedin = form.cleaned_data['linkedin']
                telegram = form.cleaned_data['telegram']
                instagram = form.cleaned_data['instagram']
                form.cleaned_data['category_resume'] = request.POST.get('category')

                if not (github.startswith('https://github') or github == ""):
                    if request.LANGUAGE_CODE == 'uz':
                        messages.error(request, "Iltimos! Githup Linkni To'gri Kiriting !!")
                    elif request.LANGUAGE_CODE == 'ru':
                        messages.error(request, "Пожалуйста! Введите ссылку Githup правильно !!")
                    else:
                        messages.error(request,
                                       "Please! Enter Githup Link Correctly !!")

                if not (linkedin.startswith('https://www.linkedin') or linkedin == ""):
                    messages.error(request, "Please enter a valid LinkedIn link")
                    if request.LANGUAGE_CODE == 'uz':
                        messages.error(request, "Iltimos! Linkedin Linkni To'gri Kiriting !!")
                    elif request.LANGUAGE_CODE == 'ru':
                        messages.error(request, "Пожалуйста! Введите ссылку Linkedin правильно !!")
                    else:
                        messages.error(request,
                                       "Please! Enter Linkedin Link Correctly !!")
                    return redirect('resume-create')

                if not (telegram.startswith('https://t.me/') or telegram == ""):
                    if request.LANGUAGE_CODE == 'uz':
                        messages.error(request, "Iltimos! Telegram Linkni To'gri Kiriting !!")
                    elif request.LANGUAGE_CODE == 'ru':
                        messages.error(request, "Пожалуйста! Введите ссылку Telegram правильно !!")
                    else:
                        messages.error(request,
                                       "Please! Enter Telegram Link Correctly !!")
                    return redirect('resume-create')

                if not (instagram.startswith('https://www.instagram.com') or instagram == ""):
                    if request.LANGUAGE_CODE == 'uz':
                        messages.error(request, "Iltimos! Instagram Linkni To'gri Kiriting !!")
                    elif request.LANGUAGE_CODE == 'ru':
                        messages.error(request, "Пожалуйста! Введите ссылку Instagram правильно !!")
                    else:
                        messages.error(request,
                                       "Please! Enter Instagram Link Correctly !!")
                    return redirect('resume-create')

                resume = form.save(commit=False)
                resume.user = request.user
                resume.save()

                if request.LANGUAGE_CODE == 'uz':
                    messages.success(request, "Muffaqiyatli Yakunlandi")
                elif request.LANGUAGE_CODE == 'ru':
                    messages.success(request, "Завершено успешно")
                else:
                    messages.success(request, "Completed successfully")
                return redirect('resume-create')
            else:
                if request.LANGUAGE_CODE == 'en':
                    messages.error(request, "Form is not valid. Please check your inputs.")
                    return redirect('resume-create')
                elif request.LANGUAGE_CODE == 'uz':
                    messages.error(request, "Shakl haqiqiy emas. Iltimos, kiritishlaringizni tekshiring.")
                    return redirect('resume-create')
                else:
                    messages.error(request, "Форма недействительна. Пожалуйста, проверьте свои записи.")
                    return redirect('resume-create')
        else:
            form = ResumeForm(request.POST, request.FILES)
            if form.is_valid():
                github = form.cleaned_data['github']
                linkedin = form.cleaned_data['linkedin']
                telegram = form.cleaned_data['telegram']
                instagram = form.cleaned_data['instagram']
                form.cleaned_data['category_resume'] = request.POST.get('category')

                if not (github.startswith('https://github') or github == ""):
                    if request.LANGUAGE_CODE == 'uz':
                        messages.error(request, "Iltimos! Githup Linkni To'gri Kiriting !!")
                    elif request.LANGUAGE_CODE == 'ru':
                        messages.error(request, "Пожалуйста! Введите ссылку Githup правильно !!")
                    else:
                        messages.error(request,
                                       "Please! Enter Githup Link Correctly !!")

                if not (linkedin.startswith('https://www.linkedin') or linkedin == ""):
                    if request.LANGUAGE_CODE == 'uz':
                        messages.error(request, "Iltimos! Linkedin Linkni To'gri Kiriting !!")
                    elif request.LANGUAGE_CODE == 'ru':
                        messages.error(request, "Пожалуйста! Введите ссылку Linkedin правильно !!")
                    else:
                        messages.error(request,
                                       "Please! Enter Linkedin Link Correctly !!")
                    return redirect('resume-create')
                if not (telegram.startswith('https://t.me/') or telegram == ""):
                    if request.LANGUAGE_CODE == 'uz':
                        messages.error(request, "Iltimos! Telegram Linkni To'gri Kiriting !!")
                    elif request.LANGUAGE_CODE == 'ru':
                        messages.error(request, "Пожалуйста! Введите ссылку Telegram правильно !!")
                    else:
                        messages.error(request,
                                       "Please! Enter Telegram Link Correctly !!")
                    return redirect('resume-create')

                if not (instagram.startswith('https://www.instagram.com') or instagram == ""):
                    if request.LANGUAGE_CODE == 'uz':
                        messages.error(request, "Iltimos! Instagram Linkni To'gri Kiriting !!")
                    elif request.LANGUAGE_CODE == 'ru':
                        messages.error(request, "Пожалуйста! Введите ссылку Instagram правильно !!")
                    else:
                        messages.error(request,
                                       "Please! Enter Instagram Link Correctly !!")
                    return redirect('resume-create')

                resume = form.save(commit=False)
                resume.user = request.user
                resume.save()

                if request.LANGUAGE_CODE == 'uz':
                    messages.success(request, "Muffaqiyatli Yakunlandi")
                elif request.LANGUAGE_CODE == 'ru':
                    messages.success(request, "Завершено успешно")
                else:
                    messages.success(request, "Completed successfully")
                return redirect('resume-create')
            else:
                if request.LANGUAGE_CODE == 'en':
                    messages.error(request, "Form is not valid. Please check your inputs.")
                    return redirect('resume-create')
                elif request.LANGUAGE_CODE == 'uz':
                    messages.error(request, "Shakl haqiqiy emas. Iltimos, kiritishlaringizni tekshiring.")
                    return redirect('resume-create')
                else:
                    messages.error(request, "Форма недействительна. Пожалуйста, проверьте свои записи.")
                    return redirect('resume-create')
    return render(request, 'resume-form.html', {"form": form, "resume": resume})


def resume_list(request, pk):

    obj = Resume.objects.filter(category_resume_id=pk)

    return render(request, 'resume_list.html', {"objec": obj})


def resume_detail(request, pk):
    obj = Resume.objects.filter(pk=pk)
    return render(request, 'resume_detail.html', {"data": obj})


def resume_delete(request):
    obj = get_object_or_404(Resume, user_id=request.user.id)
    if obj:
        obj.delete()

        if request.LANGUAGE_CODE == 'uz':
            messages.warning(request, "Resume O'chirildi")
        elif request.LANGUAGE_CODE == 'ru':
            messages.warning(request, "Резюме удалено")
        else:
            messages.warning(request, "Resume Deleted")
        return redirect('resume-create')
    return render(request, 'resume-form.html', {"data": obj})
