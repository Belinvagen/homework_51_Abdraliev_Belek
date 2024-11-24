from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('cat_status/', views.cat_status, name='cat_status'),
]
