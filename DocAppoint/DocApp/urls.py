from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('adminlogin/',views.adminlogin_view,name='adminlogin'),
    path('adminsignin/',views.adminsignin_view,name='adminsignin'),
    path('adminsignout/',views.adminsignout_view,name='adminsignout'),
    path('adddoc/',views.adddoc_view, name='adddoc'),
    path('doctors/',views.doctors_view, name='doctors'),
    path('updatedoc/<int:id>',views.updatedoc_view, name='updatedoc'),
    path('removedoc/<int:id>',views.removedoc_view,name='removedoc'),
    path('patientapp/',views.patientapp_view,name='patientapp'),
    path('status/<int:id>',views.status_view,name='status'),
    path('generatebill/<int:id>',views.generatebill_view,name='generatebill'),
    path('removeapp/<int:id>',views.removeapp_view, name='removeapp'),
    path('bill/',views.bill_view,name='bill'),
    path('signup/',views.signup_view,name='signup'),
    path('signin/',views.signin_view,name='signin'),
    path('signout/',views.signout_view,name='signout'),
    path('alldoc/',views.alldoc_view, name='alldoc'),
    path('takeappoint/<int:id>',views.takeappoint_view,name='takeappoint'),
    path('appoint/',views.appoint_view,name='appoint'),
    path('removemyapp/<int:id>',views.removemyapp_view, name='removemyapp'),
    path('myapp/',views.myapp_view,name='myapp'),    
    path('mybill/',views.mybill_view,name='mybill'),
    path('tips',views.tips_view,name='tips'),
    path('aboutus/',views.aboutus_view, name='aboutus'),    
]