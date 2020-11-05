from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process/ninja', views.ninja),
    path('process/dojo', views.dojo),
    path('deleted', views.deleted)
]
