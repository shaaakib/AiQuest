from django.contrib import admin
from django.urls import path
from Machine_Learning.views import machine_learning, deep_learning, about
from Blogs.views import blog1
from Deep_Learning.views import deep_learning
from Data_Analysis.views import data_analysis
from About_Us.views import about_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', machine_learning),
    path('dl/', deep_learning),
    path('about/', about),
    path('blog/', blog1),
    path('deepl/', deep_learning),
    path('analysis/', data_analysis),
    path('about_us/', about_us),
]
