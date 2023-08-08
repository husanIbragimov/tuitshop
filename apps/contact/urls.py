from django.urls import path
from .views import contact, news_get_list, news_get_detail

urlpatterns = [
    path('', contact, name="contact"),
    path('news/', news_get_list, name='news-list'),
    path('news/<int:id>', news_get_detail, name='news-detail'),

]
