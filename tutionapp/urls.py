from django.urls import path
from . import views
urlpatterns=[   
    path('',views.fnhome,name='home'), 
    path('kersylb/',views.fnkersylb,name='kersylb'),
    path('master/',views.fnmaster,name='master'),
    path('teachersinfo/',views.fnteacher,name='teachersinfo'),
    path('cbsesylb/',views.fncbsesylb,name='cbsesylb'),
    path('fnk5std/',views.fnk5std,name='k5std'),
    path('contactus/',views.fncontactus,name='contactus'),
    path('usersignup/',views.fnusersignup,name="usignup"),
    path('aboutus/',views.fnaboutus,name="aboutus"),
    path('c8std/',views.fnc8std,name="c8std"),
    path('userprofilemaster/',views.fnuserprofilemaster,name='userprofilemaster'),
    path('userprofile/',views.fnuserprofile,name='userprofile'),
    path('usersecurity/',views.fnusersecurity,name='usersecurity'),
    path('stdlogin',views.fnstdlogin,name='stdlogin'),
    path('stdlogout',views.fnstdlogout,name='stdlogout')
    
]