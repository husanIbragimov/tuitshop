from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from apps.contact.models import GetInTouch, Location, Subscribe, News
from modeltranslation.admin import TranslationAdmin


class GetInTouchAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'first_name')
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'status', 'created_at')


class LocationAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'address')
    list_display = ('id', 'address', 'name', 'phone_number', 'created_at')


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'created_at')


class NewsAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'description', 'short_description','created_at')
    ordering = ('-created_at',)
    group_fieldsets = True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Location, LocationAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(GetInTouch, GetInTouchAdmin)
admin.site.register(News, NewsAdmin)
