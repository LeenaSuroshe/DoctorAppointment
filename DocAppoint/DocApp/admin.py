from django.contrib import admin
from . models import Doctor,Appointment,Bill
# Register your models here.

@admin.register(Doctor)
class DocAdmin(admin.ModelAdmin):
    list_display =['name','email','contact','spcl','ava']


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display =['docname','docemail','patientname','patientemail','appointdate','appointtime','symptoms','status','user']

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['patientname','patientemail','docname','docemail','bill','med','date','user']

# @admin.register(Feedback)
# class FeedbackAdmin(admin.ModelAdmin):
#     list_display = ['name','email','contact','fdb']