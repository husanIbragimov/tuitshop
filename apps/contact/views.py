from django.http import Http404

from apps.contact.models import GetInTouch, Location, Subscribe, News
from .forms import GetInTouchForm
from django.contrib import messages
from django.shortcuts import render, redirect


def get_in_touch(request):
    form = GetInTouchForm(request.POST or None)
    try:
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully send your message")
            return redirect('/contact/')
        return render(request, 'page-contact.html', {'form': form})
    except:
        return render(request, 'page-404.html', {})


def contact(request):
    locations = Location.objects.all()

    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    phone_number = request.POST.get('telephone')
    message = request.POST.get('message')
    sbb = request.POST.get('sbb')

    if request.method == 'POST':
        GetInTouch.objects.create(first_name=first_name, last_name=last_name, phone_number=phone_number,
                                  message=message)
        Subscribe.objects.create(email=sbb)
    return render(request, 'page-contact.html', {'locations': locations})


def news_get_list(request):
    context = News.objects.all()
    return render(request, 'news.html', {"news": context})


def news_get_detail(request, id):
    context = News.objects.filter(id=id)
    if context:
        for item in context.all():
            return render(request, 'news-details.html', {"news": item})
    return Http404
