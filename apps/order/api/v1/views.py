from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.order.models import Order
from apps.product.models import ProductImage


@api_view(['POST'])
def change_status(request, *args, **kwargs):
    status = request.data.get('status')
    id = request.data.get('id')
    order = get_object_or_404(Order, id=id)
    order.status = status
    order.save()
    return Response({
        "msg": "Success",
        "status": 200
    }, status=200)

@api_view(['GET'])
def count_products(request, *args, **kwargs):
    product_images = ProductImage.objects.all()
    number = 0
    data = [{
        'color_id': None,
        'product_id': None
    }]
    for i in product_images:
        res = {
            'color_id': i.color_id,
            'product_id': i.product_id,
        }
        # if i.color_id != data['color_id'] and i.product_id != data['product_id']:
        if res not in data:
            result = product_images.filter(color_id=i.color_id, product_id=i.product_id)
            data.append(res)
            if result.exists():
                number += 1
    # print(number)
    # result = ProductImage.objects.values('product', 'color').annotate(dcount=Count('product')).order_by()
    # print(result)
    return Response({
        "msg": number,
        "status": 200
    }, status=200)
