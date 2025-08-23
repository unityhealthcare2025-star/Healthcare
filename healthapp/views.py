from django.shortcuts import render, redirect
from django.views import View

from healthapp.models import *
from healthapp.forms import *
from django.shortcuts import render, redirect
from django.views import View
from .models import *  # Adjust import based on your project structure



# Create your views here.

# ///////////////////////////////// ADMIN /////////////////////////////////////////

class LoginPage(View):
    def get(self, request):
        return render(request, "Administration/Login.html")
    
    def post(self,request):
        username=request.POST['Username']
        password=request.POST['Password']
        try:
            user=LoginTable.objects.get(Username=username,Password=password)
            request.session['login_id'] = user.id
            if user.UserType=='admin':
                return render(request,'Administration/AdminHome.html')
            elif user.UserType=='Hospital':
                return render(request,'Hospital/HospitalHome.html')
            elif user.UserType=='Doctor':
                
                return render(request,'Doctor/DoctorHome.html')
        except LoginTable.DoesNotExist:
            return render(request,'"Administration/Login.html',{'error':'Invalid username or password'})

class AdminHome(View):
    def get(self,request):
        return render(request,"Administration/AdminHome.html")    
    
class VerifyHospital(View):
    def get(self, request):
        # Show only hospitals that are pending verification
        obj = HospitalTable.objects.all()
        return render(request, "Administration/verifyHsptl.html", {'val': obj})
    
class AcceptHospital(View):
    def get(self, request, lid):
        obj = LoginTable.objects.get(id=lid)
        obj.UserType = "Hospital"
        obj.save()
        return redirect('VerifyHospital')
    
class RejectHospital(View):
    def get(self, request, lid):
        obj = LoginTable.objects.get(id=lid)
        obj.UserType = "rejected"  # Optional: distinguish rejected from pending
        obj.save()
        return redirect('VerifyHospital')

# class DeleteUser(View):
#     def get(self,request,)
#         obj = 

class ViewDoctorRating(View):
    def get(self,request):
      obj = FeedbackTable.objects.all()
      return render(request, "Administration/ViewDrRating.html", {'val': obj})

class ViewUser(View):
    def get(self,request):
        obj = UserTable.objects.all()
        return render(request, "Administration/ViewUser.html", {'val': obj})

class DeleteUser(View):
    def get(self,request, lid):
        obj = LoginTable.objects.get(id=lid)
        obj.delete()
        return redirect('ViewUser')

 
# //////////////////////////////// HOSPITAL ////////////////////////////////////////////
    
class HospitalHome(View):
    def get(self,request):
        return render(request,"Hospital/HospitalHome.html")
    
class Registration(View):
    def get(self,request):
        return render(request, "Hospital/Reg.html")
    def post(self,request):
        form=RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            f=form.save(commit=False)
            f.LOGIN=LoginTable.objects.create(Username=request.POST['Username'],Password=request.POST['Password'],UserType='pending')
            f.save()
            return redirect('/')
    
class ChangePassword(View):
    def get(self,request):
        return render(request, "Hospital/ChangePassword.html")
    
class AddDoctor(View):
    def get(self,request):
        return render(request, "Hospital/AddDoctor.html")
    def post(self,request):
        print(request.POST)
        form=Add_doctorForm(request.POST,request.FILES)
        if form.is_valid():
            f=form.save(commit=False)
            f.LOGINID=LoginTable.objects.create(Username=request.POST['UserName'],Password=request.POST['Password'],UserType='Doctor')
            f.save()
            return redirect('ManageDoctor')
        

    
class ComplaintReply(View):
    def get(self,request):
        obj = ComplaintTable.objects.all()
        return render(request, "Hospital/ComplaintReply.html",{'val':obj})
    
class ManageDoctor(View):
    def get(self,request):
        obj = DoctorTable.objects.all()
        return render(request, "Hospital/ManageDoctor.html",{'val':obj})
    
class EnrollDoctor(View):
    def get(self,request):
        return render(request, "Hospital/AddDoctor.html")
    def post(self,request):
        form= Add_doctorForm(request.POST,request.FILES)
        if form.is_valid():
            f=form.save(commit=False)
            f.LOGIN=LoginTable.objects.create(Username=request.POST['Username'],Password=request.POST['Password'],UserType='Doctor')
            f.save()
            return redirect('/')
    
class Response(View):
    def get(self,request):
        return render(request, "Hospital/Response.html")
    
class UpdateProfile(View):
    def get(self,request):
        obj = HospitalTable.objects.get(LOGIN__id=request.session['login_id'])
        return render(request, "Hospital/Updateprofile.html",{'val':obj})
    
class viewProfile(View):
    def get(self,request):
        obj = HospitalTable.objects.get(LOGIN__id=request.session['login_id'])
        return render(request, "Hospital/viewProfile.html",{'val':obj})
    
class DeleteDoctor(View):
    def get(self,request, lid):
        obj = DoctorTable.objects.get(id=lid)
        obj.delete()
        return redirect('ManageDoctor')

class EditDoctor(View):
    def get(self,request,lid):
        obj = DoctorTable.objects.get(id=lid)
        return render(request,"Hospital/EditDrProfile.html",{'val':obj})


class EditDrProfile(View):
    def get(self,request):
        obj = DoctorTable.objects.get(LOGIN__id=request.session['login_id'])
        return render(request, "Hospital/EditDrProfile.html",{'val':obj})

    
# ////////////////////////DOCTOR//////////////////////////////////

class DoctorHome(View):
    def get(self,request):
        return render(request,"Doctor/DoctorHome.html")
    
class ManageSchedule(View):
    def get(self,request):
        obj = ScheduleTable.objects.all()
        return render(request, "Doctor/ManageSchedule.html",{'val':obj})
    
class ViewBooking(View):
    def get(self,request):
        obj = BookingTable.objects.all()
        return render(request, "Doctor/ViewBooking.html",{'val':obj})
    
class Updateprofile(View):
    def get(self,request):
        obj = DoctorTable.objects.get(LOGIN__id=request.session['login_id'])
        return render(request, "Doctor/Updateprofile.html", {'val':obj, 'DOB': str(obj.DOB)})
    
class ViewComplaints(View):
    def get(self,request):
        obj = ComplaintTable.objects.all()
        return render(request, "Doctor/ViewComplaints.html",{'val':obj})

