from django.shortcuts import render
from django.http import HttpResponse
from . forms import TeacherRegistration


# Create your views here.
def blog1(request):
    return render(request, 'blogs/blogs.html')

def showformsdata(request):
    fm = TeacherRegistration()
    fm.order_fields(field_order=['email', 'last_name', 'first_name'])
    return render(request, 'blogs/forms.html', {'forms':fm})