from django.urls import path, include

urlpatterns = [
    path('api/', include('apps.order.api.v1.urls'))
]
