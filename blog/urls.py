from django.urls import path
from . import views

urlpatterns = [
    path('', views.sparta),
    path('query/', views.bd),
    path('write/', views.write)
]
