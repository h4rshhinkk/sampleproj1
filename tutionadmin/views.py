from select import select
from django.shortcuts import redirect, render
from django.http import HttpResponse

from tutionapp.models import UserRegistration,Contactus,TeacherRegistration
# from .models import TeacherRegistration
# Create your views here.

def fntadmin(request):
    return HttpResponse("Welcome to Admin")
def fnhworld(request):
    return render(request,'hello.html')
def fnadminmaster(request):
    return render(request,'adminmaster.html')
def fnadmindash(request):
    return render(request,'admindashboard.html')

def fnadminteach(request):
    TeachersDetails = TeacherRegistration.objects.all()


    return render(request,'adminteacher.html',{'dispteachdetails':TeachersDetails})




def fnteachreg(request):
    if request.method == 'POST':
        tname=request.POST['teachname']
        selectboard=request.POST['selectboard']
        teachclass=request.POST['teachselectclass']
        teachsubject=request.POST['teachselectsubject']
        teachplace=request.POST['place']
        teachphone=request.POST['phone']
        teachemail=request.POST['email']
        teachpassword=request.POST['password']
       
        TeachDetails = TeacherRegistration(TeacherName=tname,TeacherBoard=selectboard,TeacherClass=teachclass,TeacherSubject=teachsubject,
        TeacherPhone=teachphone,TeacherPlace=teachplace,TeacherEmail=teachemail,TeacherPassword=teachpassword)
        TeachDetails.save()

    return redirect('/admin/adminteacher')





#displayStudentDetails    
def fnadminstd(request):
    stddetails=UserRegistration.objects.all()

    return render(request,'adminstudents.html',{'dispstddetails':stddetails})

    
def fnadminpay(request):
    return render(request,'adminpayments.html')

    
def fnadminreq(request):
    msgdetails=Contactus.objects.all()

    return render(request,'adminrequests.html',{'dispreqmsgs':msgdetails})


def fnadminbook(request):
    return render(request,'adminbooking.html')
