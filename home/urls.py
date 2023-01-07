from django.conf.urls import url
from . import views
urlPatterns = [
    path('', views.Home),
    path('profile/', views.update_profile),
    url('account/logout/', views.logout),
]