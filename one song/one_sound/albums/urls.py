from django.urls import path
from . import views

urlpatterns = [
    path('', views.albums_list, name='albums'),
    path('albums/', views.album_list, name='album_list'),
    path('<int:album_id>/', views.album_detail, name='album_detail'),
    ]