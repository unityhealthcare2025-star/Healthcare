from django.shortcuts import render
from django.views import View

from healthapp.models import *

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
            request.session['lid']=user.id
            if user.UserType=='admin':
                return render(request,'Administration/AdminHome.html')
            elif user.UserType=='Hospital':
                return render(request,'Hospital/HospitalHome.html')
            elif user.UserType=='Doctor':
                return render(request,'Doctor/DoctorHome.html')
        except LoginTable.DoesNotExist:
            return render(request,'loginpage.html',{'error':'Invalid username or password'})

class AdminHome(View):
    def get(self,request):
        return render(request,"Administration/AdminHome.html")    
    
class VerifyHospital(View):
    def get(self,request):
        obj = HospitalTable.objects.all()
        return render(request, "Administration/verifyHsptl.html", {'val': obj})
    
class ViewDoctorRating(View):
    def get(self,request):
      obj = FeedbackTable.objects.all()
      return render(request, "Administration/ViewDrRating.html", {'val': obj})

class ViewUser(View):
    def get(self,request):
        obj = UserTable.objects.all()
        return render(request, "Administration/ViewUser.html", {'val': obj})

 
# //////////////////////////////// HOSPITAL ////////////////////////////////////////////
    
class HospitalHome(View):
    def get(self,request):
        return render(request,"Hospital/HospitalHome.html")
    
class Registration(View):
    def get(self,request):
        return render(request, "Hospital/Reg.html")
    
class ChangePassword(View):
    def get(self,request):
        return render(request, "Hospital/ChangePassword.html")
    
class AddDoctor(View):
    def get(self,request):
        return render(request, "Hospital/AddDoctor.html")
    
class ComplaintReply(View):
    def get(self,request):
        return render(request, "Hospital/ComplaintReply.html")
    
class ManageDoctor(View):
    def get(self,request):
        return render(request, "Hospital/ManageDoctor.html")
    
class Response(View):
    def get(self,request):
        return render(request, "Hospital/Response.html")
    
class UpdateProfile(View):
    def get(self,request):
        return render(request, "Hospital/Updateprofile.html")
    
# ////////////////////////DOCTOR//////////////////////////////////

class DoctorHome(View):
    def get(self,request):
        return render(request,"Doctor/DoctorHome.html")
    
class ManageSchedule(View):
    def get(self,request):
        return render(request, "Doctor/ManageSchedule.html")
    
class ViewBooking(View):
    def get(self,request):
        return render(request, "Doctor/ViewBooking.html")
    
class Updateprofile(View):
    def get(self,request):
        return render(request, "Doctor/Updateprofile.html")
    
class ViewComplaints(View):
    def get(self,request):
        return render(request, "Doctor/ViewComplaints.html")

