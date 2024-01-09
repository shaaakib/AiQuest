from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def machine_learning(request):
    return HttpResponse('<h1>Studymart offering lots of free & paid course</h1>')

def deep_learning(request):
    return HttpResponse('<h1>We have full deep learning course</h1>')

def about(request):
    return HttpResponse('<h1>We have available lots experienced teacher</h1>')
