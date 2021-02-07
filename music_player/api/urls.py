from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('data',views.data,name='data'),
    path('song-update/<str:pk>/',views.songUpdate,name='song_update'),
]