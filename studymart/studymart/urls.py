from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('About_Us.urls')),
    path('blog/', include('Blogs.urls')),
    path('contact/', include('Contact.urls')),
    path('data/', include('Data_Analysis.urls')),
    path('deep/', include('Deep_Learning.urls')),
    path('ml/', include('Machine_Learning.urls')),
]
