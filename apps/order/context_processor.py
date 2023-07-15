from django.contrib import messages

from .models import Cart, Wishlist
import uuid
from apps.contact.models import Subscribe
from ..base.models import Variant

from ..product.models import Currency, Category, Product


def cart_renderer(request):
    currency = Currency.objects.last()
    categories = Category.objects.filter(is_active=True)
    sbb = request.POST.get('sbb')
    subscribe = Subscribe.objects.filter(email=sbb)
    variants = Variant.objects.all().order_by('duration')
    active_variant = variants.last()
    if not subscribe.exists():
        if request.method == 'POST':
            Subscribe.objects.create(email=sbb)
    try:
        cart = Cart.objects.get(session_id=request.session['nonuser'], completed=False)
        wishlists = Wishlist.objects.filter(session_id=request.session['nonuser'])
    except:
        request.session['nonuser'] = str(uuid.uuid4())
        cart = Cart.objects.create(session_id=request.session['nonuser'])
        wishlists = None

    return {
        "cart": cart,
        "active_variant": active_variant,
        "wishlists": wishlists,
        "currency": currency,
        'categories': categories,
        # 'products': products,
        # 'hide_categories': categories
    }
