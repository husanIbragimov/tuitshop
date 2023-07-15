from django.urls import path
from apps.product.views import about, shop_list, shop_details, index, shop_images

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('shop/', shop_list, name="products_filter"),
    path('shop-images/', shop_images, name="shop-images"),
    path('shop-details/<int:id>', shop_details, name="shop-details")
]
