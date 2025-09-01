from django.shortcuts import render, redirect
from django.views import View

from healthapp.models import *
from healthapp.forms import *
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
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
            return render(request,'Administration/Login.html',{'error':'Invalid username or password'})

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
        obj = LoginTable.objects.all()
        username = request.POST['Username']
        for i in obj:
           if i.Username == username:
               return HttpResponse('''<script>alert("user already exist"); window.location="/";</script>''')
        if form.is_valid():
            f=form.save(commit=False)
            f.LOGIN=LoginTable.objects.create(Username=request.POST['Username'],Password=request.POST['Password'],UserType='pending')
            f.save()
            return redirect('/')
    
class ChangePassword(View):
    def get(self,request):
        return render(request, "Hospital/ChangePassword.html")
    
    def post(self,request):
        print("----------->")
        currentPassword = request.POST['currentPassword']
        newPassword = request.POST['newPassword']
        retypeNewPassword = request.POST['retypeNewPassword']

        obj = LoginTable.objects.get(id=request.session['login_id'])
        password=obj.Password
        print("---------password--->", password)
        if password == currentPassword:
            if newPassword == retypeNewPassword:
                obj.Password = newPassword
                obj.save()
                return HttpResponse('''<script>alert("your password is changed successfully."); window.location="/UpdateProfile";</script>''')
        else:    
            return HttpResponse('''<script>alert("Your old password was entered incorrectly.Please enter it again."); window.location="/UpdateProfile";</script>''')

    
class AddDoctor(View):
    def get(self,request):
        return render(request, "Hospital/AddDoctor.html")
    def post(self,request):
        print(request.POST)
        form=Add_doctorForm(request.POST,request.FILES)
        if form.is_valid():
            f=form.save(commit=False)
            f.LOGIN=LoginTable.objects.create(Username=request.POST['UserName'],Password=request.POST['Password'],UserType='Doctor')
            f.HOSPITAL=HospitalTable.objects.get(LOGIN_id=request.session['login_id'])
            f.save()
            return HttpResponse('''<script>alert("Your old password was entered incorrectly.Please enter it again."); window.location="/UpdateProfile";</script>''')
        

    
class ComplaintReply(View):
    def get(self,request):
        obj = ComplaintTable.objects.all()
        return render(request, "Hospital/ComplaintReply.html",{'val':obj})
    
class CompReply(View):
    def post(self,request, c_id):
        obj = ComplaintTable.objects.get(id=c_id)
        print("--------->", obj)
        reply = request.POST['Reply']
        print("----------------->", reply)
        obj.Response=reply
        obj.save()
        return HttpResponse('''<script>alert("The Reply was given Successfully"); window.location="/ComplaintReply";</script>''')
    
class SearchComplaint(View):
    def post(self,request):
        search=request.POST['search']
        obj = ComplaintTable.objects.filter(Date=search)
        return render(request, "Hospital/ComplaintReply.html",{'val':obj, 'date': search})
    
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
    def post(self,request):
        print(request.POST)
        obj = HospitalTable.objects.get(LOGIN_id=request.session['login_id'])
        form=RegistrationForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            
            return redirect('viewProfile')
        
    
    
class viewProfile(View):
    def get(self,request):
        obj = HospitalTable.objects.get(LOGIN__id=request.session['login_id'])
        return render(request, "Hospital/viewProfile.html",{'val':obj})
    
class DeleteDoctor(View):
    def get(self,request, lid):
        obj = LoginTable.objects.get(id=lid)
        obj.delete()
        return redirect('ManageDoctor')

class EditDoctor(View):
    def get(self,request,doctor_id):
        obj = DoctorTable.objects.get(id=doctor_id)
        return render(request,"Hospital/EditDrProfile.html",{'val':obj, 'dob':str(obj.DOB)})
    def post(self,request, doctor_id):
        print(request.POST)
        obj = DoctorTable.objects.get(id=doctor_id)
        form=Add_doctorForm(request.POST,request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('ManageDoctor')

class EditDrProfile(View):
    def get(self,request):
        obj = DoctorTable.objects.get(LOGIN__id=request.session['login_id'])
        return render(request, "Hospital/EditDrProfile.html",{'val':obj})

class ViewRating(View):
    def get(self,request):
        obj = FeedbackTable.objects.filter(DOCTOR__HOSPITAL__LOGIN_id=request.session['login_id'])
        return render(request,"Hospital/ViewDrRating.html",{'val':obj})
    
# ////////////////////////DOCTOR//////////////////////////////////

class DoctorHome(View):
    def get(self,request):
        return render(request,"Doctor/DoctorHome.html")
    
class ManageSchedule(View):
    def get(self,request):
        obj = ScheduleTable.objects.all()
        return render(request, "Doctor/ManageSchedule.html",{'val':obj})
    def post(self,request):
        print(request.POST)
        obj = DoctorTable.objects.get(LOGIN_id=request.session['login_id'])
        form=ManageScheduleForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.DOCTOR=obj
            f.save()
            return redirect('ManageSchedule')
        
    
class ViewBooking(View):
    def get(self,request):
        obj = BookingTable.objects.all()
        return render(request, "Doctor/ViewBooking.html",{'val':obj})
    
class UpdateDrProfile(View):
    def get(self,request):
        obj = DoctorTable.objects.get(LOGIN__id=request.session['login_id'])
        return render(request, "Doctor/UpdateDrProfile.html", {'val':obj, 'DOB': str(obj.DOB)})
    def post(self,request):
        print(request.POST)
        obj = DoctorTable.objects.get(LOGIN_id=request.session['login_id'])
        form=UpdatedoctorForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('viewDrProfile')
         

    
class viewDrProfile(View):
    def get(self,request):
        obj = DoctorTable.objects.get(LOGIN__id=request.session['login_id'])
        return render(request, "Doctor/viewDrProfile.html", {'val':obj, 'DOB': str(obj.DOB)})
    
class ViewComplaints(View):
    def get(self,request):
        obj = ComplaintTable.objects.all()
        return render(request, "Doctor/ViewComplaints.html",{'val':obj})
    

class ChangePassword1(View):
    def get(self,request):
        return render(request, "Doctor/ChangePassword1.html")
    
    def post(self,request):
        print("----------->")
        currentPassword = request.POST['currentPassword']
        newPassword = request.POST['newPassword']
        retypeNewPassword = request.POST['retypeNewPassword']

        obj = LoginTable.objects.get(id=request.session['login_id'])
        password=obj.Password
        print("---------password--->", password)
        if password == currentPassword:
            if newPassword == retypeNewPassword:
                obj.Password = newPassword
                obj.save()
                return HttpResponse('''<script>alert("your password is changed successfully."); window.location="/UpdateDrProfile";</script>''')
        else:    
            return HttpResponse('''<script>alert("Your old password was entered incorrectly.Please enter it again."); window.location="/UpdateDrProfile";</script>''')

class DeleteSchedule(View):
    def get(self,request, lid):
        obj = ScheduleTable.objects.get(id=lid)
        obj.delete()
        return redirect('ManageSchedule') 

