from django.urls import path
from . import views
urlpatterns = [
    path('deepl/', views.deep_learning),
    path('register/', views.registration),
]
