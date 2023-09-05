"""tuitshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from apps.base import views
from apps.order.api.v1 import views as api_views

from django.views.static import serve

urlpatterns = [
                  path('tuitsh-admin/', admin.site.urls),
                  re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
                  re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

              ] + i18n_patterns(
    # language
    path('i18n/', include('django.conf.urls.i18n')),
    # lib
    path('base/', include('allauth.urls')),

    # api
    path('change_status/', api_views.change_status),
    path('count-products/', api_views.count_products),
    # local apps
    path('', include('apps.product.urls')),
    path('about/', include('apps.about.api.urls')),
    path('order/', include('apps.order.urls')),
    path('contact/', include('apps.contact.urls')),

    # login & register
    path('register/', views.register, name="register"),
    path('login/', views.login_func, name="login"),
    path('logout/', views.logout_func, name="logout"),
    path('resume/', views.resume_create, name="resume-create"),
    path('resume-list/<int:pk>', views.resume_list, name="resume-list"),
    path('resume-detail/<int:pk>', views.resume_detail, name="resume-detail"),
    path('resume-delete/', views.resume_delete, name="resume-delete"),

    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = "core.errors.page_not_found_view"
