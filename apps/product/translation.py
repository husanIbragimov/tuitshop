from .models import Product, Advertisement, Category, Banner, Brand, AdditionalInfo
from modeltranslation.translator import TranslationOptions, register


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Advertisement)
class AdvertisementTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')


@register(Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(AdditionalInfo)
class AdditionalInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
