from django import forms
from . models import Doctor,Appointment,Bill
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User



class LoginForm(AuthenticationForm):

    username = forms.CharField(label='Enter Username',widget=forms.TextInput(attrs={'class':'form-control'}))

    password = forms.CharField(label='Enter Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))    



spcl_choices = [("Allergist", 'Allergist'), ("Cardiologist", "Cardiologist"), ("Dermatologist", "Dermatologist"), ('ENT', 'ENT'), ("General Practitioners", "General Practitioners"), ("Gynecologists", "Gynecologists"), ('Psychiatrist', 'Psychiatrist'), ("Psychologists", "Psychologists"), ('Surgeons', 'Surgeons')]


class DocForm(forms.ModelForm):
    spcl = forms.MultipleChoiceField(choices=spcl_choices, label='Specialization', widget=forms.CheckboxSelectMultiple)

    class Meta:
        model=Doctor
        fields=['name','email','contact','spcl','ava']

        labels={
            'name':'Doctor Name',
            'email':'Doctor Email',
            'contact':'Contact Number',
            'ava':'Availability'
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'contact':forms.TextInput(attrs={'class':'form-control'}),
            'ava':forms.TextInput(attrs={'class':'form-control'}),
        }


time_choices = [("9am-10am", "9am-10am"), ("10am-11am", "10am-11am"), ('11am-12pm', '11am-12pm'), ("12pm-1pm", "12pm-1pm"), ("2pm-3pm", "2pm-3pm"), ("3pm-4pm", "3pm-4pm"), ("4pm-5pm", "4pm-5pm"), ("5pm-6pm", "5pm-6pm"), ("6pm-7pm", "6pm-7pm"), ("7pm-8pm", "7pm-8pm")]

class AppointForm(forms.ModelForm):

    appointtime = forms.ChoiceField(choices=time_choices, label='Appointment Time', widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model=Appointment
        fields=['docname','docemail','patientname','patientemail','appointdate','appointtime','symptoms','user']

        labels={
            'docname':'Doctor Name',
            'docemail':'Doctor Email',
            'patientname':'Patient Name',
            'patientemail':'Patient Email',
            'appointdate':'Appointment Date',
            'symptoms':'Symptoms',
            'user':'Enter your Username'
        }

        widgets = {
            'docname':forms.TextInput(attrs={'class':'form-control'}),
            'docemail':forms.EmailInput(attrs={'class':'form-control'}),
            'patientname':forms.TextInput(attrs={'class':'form-control'}),
            'patientemail':forms.EmailInput(attrs={'class':'form-control'}),
            'appointdate':forms.DateInput(attrs={'class':'form-control'}),
            'appointtime':forms.TextInput(attrs={'class':'form-control'}),
            'symptoms':forms.TextInput(attrs={'class':'form-control'}),
            'user':forms.TextInput(attrs={'class':'form-control'}),
        }



class RegisterForm(UserCreationForm):

    password1 = forms.CharField(label='Enter Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2 = forms.CharField(label ='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

        labels = {'username':'Enter Username','first_name':'Enter First Name','last_name':'Enter Last Name','email':'Enter Email-ID'}

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

class BillForm(forms.ModelForm):
    class Meta:
        model=Bill
        fields=['patientname','patientemail','docname','docemail','bill','med']

        labels={
            'patientname':'Patient Name',
            'patientemail':'Patient Email',
            'docname':'Doctor Name',
            'docemail':'Doctor Email',
            'bill':'Amount',
            'med':'Medicines'
        }

        widgets = {
            'patientname':forms.TextInput(attrs={'class':'form-control'}),
            'patientemail':forms.EmailInput(attrs={'class':'form-control'}),
            'docname':forms.TextInput(attrs={'class':'form-control'}),
            'docemail':forms.EmailInput(attrs={'class':'form-control'}),
            'bill':forms.TextInput(attrs={'class':'form-control'}),
            'med':forms.TextInput(attrs={'class':'form-control'})
        }


# class FeedbackForm(forms.ModelForm):
#     class Meta:
#         model=Feedback
#         fields=['name','email','contact','fdb']

#         labels={
#             'name':'Name',
#             'email':'Email',
#             'contact':'Contact',
#             'fdb':'Feedback',
#         }

#         widgets = {
#             'name':forms.TextInput(attrs={'class':'form-control'}),
#             'email':forms.EmailInput(attrs={'class':'form-control'}),
#             'docname':forms.TextInput(attrs={'class':'form-control'}),
#             'contact':forms.TextInput(attrs={'class':'form-control'}),
#             'fdb':forms.Textarea(attrs={'class':'form-control'})
#         }
