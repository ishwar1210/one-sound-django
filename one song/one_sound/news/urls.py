from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('list/', views.news_list, name='news_list')
]
