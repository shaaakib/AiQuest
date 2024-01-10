from django.shortcuts import render

# Create your views here.
def contact(request):
    con = {'c' : 'Hello I am create contact page'}
    return render(request, 'contact/contact.html', context=con)