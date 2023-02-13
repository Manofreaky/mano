from django.shortcuts import render

# Create your views here.
def welcome(request):
    
    return render(request,'home.html')
def labour(request):
    return render(request,'labour.html')

def owner(request):
    return render(request,'form.html')