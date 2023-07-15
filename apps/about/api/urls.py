from django.urls import path, include

urlpatterns = [
    path('api/', include('apps.about.api.v1.urls'))
]
