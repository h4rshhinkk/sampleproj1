from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fndemo(request):
    return render(request,'demo.html')
def fnteachmaster(request):
    return render(request,'teachmaster.html')
def fnteachdash(request):
    return render(request,'teachdash.html')
def fnteachstudents(request):
    return render(request,'teachstudent.html')
def fnteachpayment(request):
    return render(request,'teachpayment.html')
def fnteachprofile(request):
    return render(request,'teachprofile.html')