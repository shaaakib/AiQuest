from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def machine_learning(request):
    return render(request,'machine_learning.html')