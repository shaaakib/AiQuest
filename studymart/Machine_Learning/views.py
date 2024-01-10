from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def machine_learning(request):
    teacher = {'names': ['Shakib','Shakil','Mejba','Sohanur']}
    return render(request,'machine_learning/machine_learning.html', context=teacher)

def random(request):
    return render(request,'machine_learning/random_forest.html')

def dtrees(request):
    return render(request,'machine_learning/dt.html')

def k_nearest(request):
    return render(request,'machine_learning/knn.html')