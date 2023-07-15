from django.contrib import admin
from django.dispatch import receiver
from mptt.admin import DraggableMPTTAdmin
from import_export.admin import ImportExportModelAdmin
import admin_thumbnails
from apps.product.forms import BannerFrom
from apps.product.models import Category, Brand, Banner, Product, ProductImage, Rate, Advertisement, Color, \
    AdditionalInfo, Currency, Size, BannerDiscount
from modeltranslation.admin import TranslationAdmin
from import_export.signals import post_import, post_export

from apps.product.resources import ProductImageResource


class BannerAdmin(TranslationAdmin):
    form = BannerFrom


@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = ('id',)
    extra = 1


@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image', 'product', 'image_thumbnail']


class CategoryAdmin(DraggableMPTTAdmin, TranslationAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title', 'created_at', 'is_active', 'id')

    list_display_links = ('indented_title', 'id')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
    list_per_page = 25


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImage
    extra = 1


class AdditionalInfoAdmin(admin.StackedInline):
    model = AdditionalInfo
    extra = 1
    list_display = ['id', "title", 'product', "description"]
    list_filter = ['prodcut', 'created_at']


class ProductAdmin(TranslationAdmin):
    actions = ['make_published']
    inlines = [ProductImageInline, AdditionalInfoAdmin]
    filter_horizontal = ('category', 'size')
    list_display_links = ('id', 'title')
    list_display = (
        'title', 'percentage', 'discount', 'get_discount_price', 'mid_rate', 'view', 'is_active',
        'id')
    search_fields = ('title', )
    readonly_fields = ('mid_rate', 'get_discount_price',)
    list_filter = ('is_active', 'status', 'brand', 'updated_at', 'created_at')
    list_per_page = 50

    group_fieldsets = True

    @admin.action(description='Mark selected stories as published')
    def make_published(modeladmin, request, queryset):
        queryset.create(status='NEW')

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class BrandTranslationAdmin(TranslationAdmin):
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


class AdvertisementAdmin(TranslationAdmin):
    list_display = ['id', "title", "description"]

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


class BannerTranslationAdmin(TranslationAdmin):
    group_fieldsets = True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
               }


@admin.register(ProductImage)
class ProductImageAdmin(ImportExportModelAdmin):
    list_display = ("id", "color", "price")
    resource_classes = [ProductImageResource]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.order_by('color__name', 'product__id', '-id').distinct("color__name", "product__id")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandTranslationAdmin)
admin.site.register(AdditionalInfo)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Banner, BannerTranslationAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Rate)
admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(Currency)
admin.site.register(BannerDiscount)
