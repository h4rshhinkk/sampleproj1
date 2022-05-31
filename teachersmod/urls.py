from django.urls import path
from . import views
urlpatterns=[   
    path('demo',views.fndemo,name='demo'),
     path('teachmaster',views.fnteachmaster,name='teachmaster'),
    path('teachdash',views.fnteachdash,name='teachdash'),
    path('teachstudents',views.fnteachstudents,name='teachstudents'),
    path('teachpayment',views.fnteachpayment,name='teachpayment'),
    path('teachprofile',views.fnteachprofile,name='teachprofile'),
]