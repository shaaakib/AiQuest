from django.urls import path
from . import views
urlpatterns = [
    path('machine/', views.machine_learning),
    path('dt/', views.dtrees),
    path('rn/', views.random),
    path('knn/', views.k_nearest),

]
