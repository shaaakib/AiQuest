from django.urls import path
from . import views
urlpatterns = [
    path('machine/', views.machine_learning),
    path('dl/', views.deep_learning),
    path('about/', views.about),
]
