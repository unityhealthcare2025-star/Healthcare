from django.shortcuts import render, redirect
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
    def get(self,request):
        obj = HospitalTable.objects.all()
        return render(request, "Administration/verifyHsptl.html", {'val': obj})
    
class AcceptHospital(View):
    def get(self,request, lid):
        obj = LoginTable.objects.get(id=lid)
        obj.UserType = "Hospital"
        obj.save()
        return redirect('VerifyHospital')
    
class RejectHospital(View):
    def get(self,request, lid):
        obj = LoginTable.objects.get(id=lid)
        obj.UserType="pending"
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
    
class ChangePassword(View):
    def get(self,request):
        return render(request, "Hospital/ChangePassword.html")
    
class AddDoctor(View):
    def get(self,request):
        return render(request, "Hospital/AddDoctor.html")
    
class ComplaintReply(View):
    def get(self,request):
        obj = ComplaintTable.objects.all()
        return render(request, "Hospital/ComplaintReply.html",{'val':obj})
    
class ManageDoctor(View):
    def get(self,request):
        obj = DoctorTable.objects.all()
        return render(request, "Hospital/ManageDoctor.html",{'val':obj})
    
class Response(View):
    def get(self,request):
        return render(request, "Hospital/Response.html")
    
class UpdateProfile(View):
    def get(self,request):
        obj = HospitalTable.objects.get(LOGIN__id=request.session['login_id'])
        return render(request, "Hospital/Updateprofile.html",{'val':obj})
    
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

