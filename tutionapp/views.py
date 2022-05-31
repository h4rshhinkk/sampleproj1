# from ctypes import addressof
import email
from django.shortcuts import redirect, render
from .models import UserRegistration,Contactus


# from django.views.decorators.http import require_http_methods
# from decorator import user_login_required
# Create your views here.
def fnhome(request):
    return render(request,'home.html')
def fnkersylb(request):
    return render(request,'kersylb.html')
def fnmaster(request):
    return render(request,'master.html')
def fnteacher(request):
    return render(request,'teachers.html')
def fncbsesylb(request):
    return render(request,'cbsesylb.html')
def fnk5std(request):
    return render(request,'k5std.html')
def fncontactus(request):
    if request.method == 'POST':
        rname=request.POST['eqname']
        remail=request.POST['eqemail']
        rmobile=request.POST['eqnumber']
        rmsg=request.POST['eqmessage']
        reqinfo = Contactus(ReqName=rname,ReqEmail=remail,ReqMobile=rmobile,ReqMessage=rmsg)
        reqinfo.save()
        return render(request,'contactus.html',{'status': 'Your Enquiry send Successfully'})



    return render(request,'contactus.html')

def fnusersignup(request):
    if request.method == 'POST':
        sname=request.POST['studentname']
        pname=request.POST['parentname']
        gender=request.POST['selectgender']
        studentboard=request.POST['selectboard']
        studentclass=request.POST['selectclass']
        schoolname=request.POST['schoolname']
        stdaddress=request.POST['address']
        email=request.POST['email']
        stdphone=request.POST['studentphone']
        pphone=request.POST['parentphone']
        password=request.POST['password']
        RegDetails = UserRegistration(StudentName=sname,ParentName=pname,Gender=gender,Board=studentboard,
        StudentClass=studentclass,SchoolName=schoolname,Address=stdaddress,StudentEmail=email,
        StudentPhone=stdphone,ParentPhone=pphone,StudentPassword=password)
        RegDetails.save()
        return render(request,'home.html',{'status': 'Successfully Registered'})
    else:
        return render(request,'usersignup.html')

def fnaboutus(request):
    return render(request,'aboutus.html')
def fnc8std(request):
    return render(request,'c8std.html')
def fnuserprofilemaster(request):
    return render(request,'userprofilemaster.html')





def fnusersecurity(request):
    return render(request,'usersecurity.html')

def fnstdlogin(request):
    if request.method == 'POST':
        username=request.POST['uemail']
        password=request.POST['password']

        try:
            logindata=UserRegistration.objects.get(StudentEmail=username,StudentPassword=password)
            request.session['userid'] = logindata.id
            return redirect('home')

        except UserRegistration.DoesNotExist:
            return render(request,"home.html",{'error':'Invalid User'})
    else:
        return render(request,"home.html")



def fnuserprofile(request):
    if request.method == 'POST':
       email=request.POST['changeemail']
       sphone=request.POST['changestdphone']
       print(email)
       change=UserRegistration.objects.filter(id=request.session['userid']).update(StudentEmail=email,StudentPhone=sphone)
       return redirect('userprofile')

    else:
        id=request.session['userid']
        userDetails=UserRegistration.objects.get(id=id)
        
        return render(request,'userprofile.html',{'std_details':userDetails})



def fnstdlogout(request):
    del request.session['userid']
    return redirect('home')

