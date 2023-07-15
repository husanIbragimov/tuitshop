from django.urls import path
from apps.order.views import add_to_cart, review, shop_cart, delete_cart_item, create_order, wishlist, delete_wishlist, \
    wishlist_list, create_order_wishlist, account, confirm_order

urlpatterns = [
    path('my-account/', account, name="my-account"),
    path('add-to-cart/', add_to_cart, name="add-to-cart"),
    path('shop-cart/', shop_cart, name="shop-cart"),
    path('create-order/<int:id>', create_order, name="create-order"),
    path('confirm-order/', confirm_order, name="confirm-order"),
    path('wishlist/', wishlist_list, name="wishlist"),
    path('wishlist/<int:id>', wishlist, name="wishlist"),
    path('delete-wishlist/<int:id>', delete_wishlist, name="delete-wishlist"),
    path('delete-cart-item/<int:id>', delete_cart_item, name="delete-cart-item"),
    path('create_order_wishlist/<int:id>', create_order_wishlist, name="create_order_wishlist"),
    path('review/', review, name="review")
]
