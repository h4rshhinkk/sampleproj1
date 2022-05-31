from django.urls import path
from . import views
urlpatterns=[   
    path('tadmin',views.fntadmin,name='tadmin'),
    path('helloworld',views.fnhworld,name='helloworld'), 
    path('adminmaster',views.fnadminmaster,name='adminmaster'),
    path('admindashboard',views.fnadmindash,name='admindashboard'),
    path('adminteacher',views.fnadminteach,name='adminteacher'),
    path('adminstudents',views.fnadminstd,name='adminstudent'),
    path('adminpayments',views.fnadminpay,name='adminpayment'),
    path('adminrequests',views.fnadminreq,name='adminrequests'),
    path('adminbooking',views.fnadminbook,name='fnadminbooking'),
    path('teachreg',views.fnteachreg,name='teachreg'),
   


    
    
]