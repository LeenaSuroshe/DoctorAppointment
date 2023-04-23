from django.shortcuts import render, redirect
from . models import Doctor, Appointment, Bill
from . forms import DocForm,AppointForm,LoginForm,RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def home_view(request):
    formss = LoginForm()
    context = {'formss':formss}
    return render(request, 'DocApp/home.html',context)

# ----------------Admin Views----------------------------

def adminlogin_view(request):
    formss = LoginForm()
    context = {'formss':formss}
    return render(request,'DocApp/adminlogin.html',context)


def adminsignin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']

        user = authenticate(username = username ,password = pass1)
        if user is not None:
            if user.is_staff:
                login(request,user)
                messages.success(request,'Successfully Admin login..')
                return redirect('patientapp')
            else:
                messages.warning(request,'Incorrect Admin Information')
                return redirect('adminlogin')

        else:
            messages.warning(request,'Something Went Wrong..!!')
            return redirect('adminlogin')

    return redirect('home')


def adminsignout_view(request):
    logout(request)
    messages.success(request,'Successfully Admin LogOut')
    return redirect('home')


def adddoc_view(request):
    forms = DocForm()
    context = {'forms': forms}
  
    if request.method=='POST':
        new_name=request.POST['name']
        new_email=request.POST['email']
        new_contact=request.POST['contact']
        new_spcl=request.POST['spcl']
        new_ava=request.POST['ava']
        doc=Doctor(name=new_name, email=new_email, contact=new_contact, spcl=new_spcl, ava=new_ava)
        doc.save()
        messages.success(request,'Successfully Doctor Added')
        return redirect('doctors')
    return render(request,'DocApp/adddoc.html',context)


def doctors_view(request):
    doct=Doctor.objects.all()
    context={'doct':doct}
    return render(request,'DocApp/doctors.html',context)

def updatedoc_view(request, id):
    app=Doctor.objects.get(id=id)
    context={'app':app}

    if request.method=='POST':
        new_name=request.POST['name']
        new_email=request.POST['email']
        new_contact=request.POST['contact']
        new_spcl=request.POST['spcl']
        new_ava=request.POST['ava']

        app.name=new_name
        app.email=new_email
        app.contact=new_contact
        app.spcl=new_spcl
        app.ava=new_ava
        app.save()
        return redirect('doctors')

    return render(request,'DocApp/updatedoc.html',context)

def removedoc_view(request,id):
    app=Doctor.objects.get(id=id)
    app.delete()
    return redirect('doctors')


def patientapp_view(request):
    app=Appointment.objects.all().order_by('appointdate','appointtime')
    context={'app':app}
    return render(request, 'DocApp/patientapp.html',context)


def status_view(request,id):
    app=Appointment.objects.get(id=id)
    context={'app':app}
    if request.method=='POST':
        new_status=request.POST['status']
        app.status=new_status
        app.save()
        return redirect('patientapp')
    return render(request,'DocApp/status.html',context)


def generatebill_view(request,id):
    bill=Appointment.objects.get(id=id)
    context={'bill':bill}

    if request.method == 'POST':
        patientname=request.POST['patientname']
        patientemail=request.POST['patientemail']
        docname=request.POST['docname']
        docemail=request.POST['docemail']
        bill=request.POST['bill']
        med=request.POST['med']
        user=request.POST['user']
        bill=Bill(patientname=patientname,patientemail=patientemail,docname=docname,docemail=docemail,bill=bill,med=med,user=user)
        bill.save()
        messages.success(request,'Successfully bill generated...')
        return redirect('bill')
    
    return render(request,'DocApp/generatebill.html',context)

def removeapp_view(request,id):
    app=Appointment.objects.get(id=id)
    app.delete()
    return redirect('patientapp')
    

def bill_view(request):
    bill=Bill.objects.all().order_by('date')
    context={'bill':bill}
    return render(request, 'DocApp/bill.html',context)



# -----------------------Patient Views----------------------



def signup_view(request):
    forms = RegisterForm()

    if request.method == 'POST':
        forms = RegisterForm(request.POST)
        if forms.is_valid():

            forms.save()
            messages.success(request,'Succesfully User Registered..')
            return redirect('home')

    context ={'forms':forms}
    return render(request,'DocApp/signup.html',context)


def signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']

        user = authenticate(username = username ,password = pass1)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully User login..')
    
            return redirect('alldoc')

        else:
            messages.warning(request,'Something Went Wrong..!!')
            return redirect('home')

    return redirect('home')


def signout_view(request):
    logout(request)
    messages.success(request,'Successfully User LogOut')
    return redirect('home')


def alldoc_view(request):
    doc=Doctor.objects.all()
    context={'doc':doc}
    return render(request, 'DocApp/alldoc.html',context)


def takeappoint_view(request, id):
    app=Doctor.objects.get(id=id)
    context={'app':app}

    try:
        if request.method == 'POST':
            docname=request.POST['docname']
            docemail=request.POST['docemail']
            patientname=request.POST['patientname']
            patientemail=request.POST['patientemail']
            appointdate=request.POST['appointdate']
            appointtime=request.POST['appointtime']
            symptoms=request.POST['symptoms']
            user=request.POST['user']
            app=Appointment(docname=docname,docemail=docemail,patientname=patientname,patientemail=patientemail,appointdate=appointdate,appointtime=appointtime,symptoms=symptoms,user=user)
            app.save()
            messages.success(request,'Appointment successfully registered...')
            return redirect('alldoc')
    except:
        messages.warning(request,'Enter date in this formate:- YYYY-MM-DD')
    
    return render(request,'DocApp/takeappoint.html',context)


def appoint_view(request):
    forms=AppointForm()
    context = {'forms': forms}

    try:
        if request.method == 'POST':
            docname=request.POST['docname']
            docemail=request.POST['docemail']
            patientname=request.POST['patientname']
            patientemail=request.POST['patientemail']
            appointdate=request.POST['appointdate']
            appointtime=request.POST['appointtime']
            symptoms=request.POST['symptoms']
            user=request.POST['user']
            app=Appointment(docname=docname,docemail=docemail,patientname=patientname,patientemail=patientemail,appointdate=appointdate,appointtime=appointtime,symptoms=symptoms,user=user)
            app.save()
            messages.success(request,'Appointment successfully registered...')
            return redirect('alldoc')
    except:
        messages.warning(request,'Date Must Be In YYYY-MM-DD Format')

    return render(request, 'DocApp/appoint.html',context)

def removemyapp_view(request,id):
    app=Appointment.objects.get(id=id)
    app.delete()
    return redirect('myapp')

def myapp_view(request):
    app=Appointment.objects.filter(user=request.user)
    context={'app':app}
    return render(request,'DocApp/myapp.html',context)


def mybill_view(request):
    bill=Bill.objects.filter(user=request.user)
    context={'bill':bill}
    return render(request, 'DocApp/mybill.html',context)

def tips_view(request):
    return render(request,'DocApp/tips.html')


def aboutus_view(request):
    return render(request,'DocApp/aboutus.html')