from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('change-password/',views.MyPasswordChangeView.as_view(),name='reset'),
]
