
from django.forms import ModelForm
from healthapp.models import *

class RegistrationForm(ModelForm):
    class Meta:
        model=HospitalTable
        fields=['UserName','Registration_no','Phone','E_mail','Address','City','State','Pincode']
class Add_doctorForm(ModelForm):
    class Meta:
        model=DoctorTable
        fields=['UserName','DOB','Gender','Specialization','Qualification','Experience_year','E_mail','Phone'] 

class UpdateHospitalForm(ModelForm):
    class Meta:
        model=HospitalTable
        fields=['UserName','Phone','E_mail','Address','City','State','Pincode']

class ResponseForm(ModelForm):
    class Meta:
        model=ComplaintTable
        fields=['Response']

class ManageScheduleForm(ModelForm):
    class Meta:
        model=ScheduleTable
        fields=['Day_of_week','Start_Time','End_Time']

class UpdatedoctorForm(ModelForm):
    class Meta:
        model=DoctorTable
        fields=['UserName','DOB','Gender','Specialization','Qualification','Experience_year','E_mail','Phone']
