from django.contrib import admin
from apps.contact.models import GetInTouch, Location, Subscribe


class GetInTouchAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'first_name')
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'status', 'created_at')


class LocationAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'address')
    list_display = ('id', 'address', 'name', 'phone_number', 'created_at')


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'created_at')


admin.site.register(Location, LocationAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(GetInTouch, GetInTouchAdmin)
