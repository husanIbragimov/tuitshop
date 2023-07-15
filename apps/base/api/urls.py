from django.urls import path, include

urlpatterns = [
    path('api/', include('apps.base.api.v1.urls'))
]
