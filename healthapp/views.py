from math import atan2, cos, radians, sin, sqrt
from django.shortcuts import render, redirect
from django.views import View

from healthapp.models import *
from healthapp.forms import *
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from healthapp.serializers import *
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
            return HttpResponse('''<script>alert("Added Successfully"); window.location="/ManageDoctor";</script>''')
        

    
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
    
def accept_booking(request, id):
    booking = BookingTable.objects.get(id=id)
    booking.Status = "Accepted"
    booking.save()
    return redirect('/ViewBooking')  # your booking list page

def reject_booking(request, id):
    booking = BookingTable.objects.get(id=id)
    booking.Status = "Rejected"
    booking.save()
    return redirect('/ViewBooking')
    
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
    

class AddPrescription(View):
    def get(self,request, id):
        bookingid = BookingTable.objects.get(id = id)
        return render(request,"Doctor/AddPrescription.html", {'c': bookingid})    
    def post(self,request, id):
        print(request.POST)
        bookingid = BookingTable.objects.get(id = id)
        form=AddPrescriptionForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.BOOKING=bookingid
            f.save()
            return redirect('DoctorHome')
        
        
        

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
    

#################################USER###########################################

from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED
from rest_framework.response import Response

class UserRegApiView(APIView):
    def post(self,request):
        print('==================',request.data)
        reg_serial=RegisterSerializer(data=request.data)
        login_serial=LoginSerializer(data=request.data)

        regvalid=reg_serial.is_valid()
        loginvalid=login_serial.is_valid()

        if regvalid and loginvalid:
            login=login_serial.save(UserType='User')
            reg_serial.save(LOGIN=login)
            return Response({'message':'Registration successful'},status=HTTP_200_OK)
        else:
            return Response({'Registration error': reg_serial.errors if not regvalid else None,
                             'login error': login_serial.errors if not loginvalid else None}, status=HTTP_400_BAD_REQUEST)
        
class loginApiView(APIView):
    def post(self,request):
        Response_dict={}
        Username=request.data.get('Username')
        Password=request.data.get('Password')
        try:
            if not Username or not Password:
                return Response({'Response': 'Login failed'}, status=HTTP_400_BAD_REQUEST)
            uname=LoginTable.objects.filter(Username=Username, Password=Password).first()
            if not uname:
                return Response({'Response':'login failed!'}, status=HTTP_400_BAD_REQUEST)
            else:
                Response_dict['message'] = 'login successful'
                Response_dict['UserType'] = uname.UserType
                Response_dict['userid'] = uname.id
                return Response(Response_dict,status=HTTP_200_OK)
        except Exception as e:
            return Response({'Response':'internal server error'},status=HTTP_500_INTERNAL_SERVER_ERROR)

class NearbyHospitalsAPIView(APIView):
    def get(self, request):
        try:
            lat = request.query_params.get('latitude')
            lon = request.query_params.get('longitude')

            if not lat or not lon:
                return Response({'error': 'Latitude and longitude are required'}, status=HTTP_400_BAD_REQUEST)

            user_lat = float(lat)
            user_lon = float(lon)

            def haversine(lat1, lon1, lat2, lon2):
                R = 6371  # Earth radius in kilometers
                dlat = radians(lat2 - lat1)
                dlon = radians(lon2 - lon1)
                a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
                c = 2 * atan2(sqrt(a), sqrt(1 - a))
                return R * c

            nearby_hospitals = []
            for hospital in HospitalTable.objects.all():
                if hospital.latitude and hospital.longitude:
                    distance = haversine(user_lat, user_lon, hospital.latitude, hospital.longitude)
                    if distance <= 5:
                        nearby_hospitals.append({
                            'id': hospital.id,
                            'name': hospital.UserName,
                            'email': hospital.E_mail,
                            'phone': hospital.Phone,
                            'address': hospital.Address,
                            'city': hospital.City,
                            'state': hospital.State,
                            'pincode': hospital.Pincode,
                            'latitude': hospital.latitude,
                            'longitude': hospital.longitude,
                            'image': hospital.Image.url if hospital.Image else None,
                            'distance_km': round(distance, 2)
                        })

            return Response({'hospitals': nearby_hospitals}, status=HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_400_BAD_REQUEST)
        


class DoctorsByHospitalAPIView(APIView):
    def get(self, request, hospital_id):
        try:
            doctors = DoctorTable.objects.filter(HOSPITAL__id=hospital_id)
            data = []
            for doc in doctors:
                data.append({
                    'id':doc.id,
                    'name': doc.UserName,
                    'email': doc.E_mail,
                    'phone': doc.Phone,
                    'specialization': doc.Specialization,
                    'experience': doc.Experience_year,
                    'qualification': doc.Qualification,
                })
            return Response({'doctors': data}, status=HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_400_BAD_REQUEST)

        
class SendComplaintsApView(APIView):
    def get(self, request, id):
        comp = ComplaintTable.objects.filter(USER__LOGIN_id=id)
        hospital = HospitalTable.objects.all()
        h_data = []
        for hos in hospital:
                h_data.append({
                    'name': hos.UserName,
                    'id': hos.id,
                
                })
        serializer = ComplaintSerializer(comp, many=True)
        return Response({
            'complaints': serializer.data,
            'hos': h_data
        })    

    def post(self,request,id):
        print(request.data)
        serializer = ComplaintSerializer(data=request.data)
        user_obj = UserTable.objects.get(LOGIN_id=id)
        if serializer.is_valid():
            serializer.save(USER=user_obj)
            return Response({'message': 'Complaint submit successfully'},status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
# class FeedbackApiView(APIView):
#     def post(self, request, id):
#         serializer = DoctorFeedbackSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save(user_id=id)
#             return Response({'message': 'Feedback sent successfully'},status=HTTP_201_CREATED)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class BookAppointmentAPIView(APIView):
    def post(self, request, id):
        try:
            user = UserTable.objects.get(LOGIN_id=id)
        except UserTable.DoesNotExist:
            return Response({'error': 'User not found'}, status=HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        serializer = BookingSerializer(data=data)

        if serializer.is_valid():
            booking = serializer.save(USER=user)
            return Response({'message': 'Appointment booked successfully', 'booking_id': booking.id}, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from django.utils.dateparse import parse_time

class DoctorAvailabilityView(APIView):
    def get(self, request, doctor_id):
        c = ScheduleTable.objects.filter(DOCTOR__id = doctor_id)
        serializer = SchedulSerailizer(c,many=True)
        print("--------------->", serializer.data)
        return Response(serializer.data,status=HTTP_200_OK)
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from .models import BookingTable, ScheduleTable, UserTable
from datetime import datetime, timedelta

class BookDoctor(APIView):
    def post(self, request, lid):
        print("Request data:", request.data)
        user = UserTable.objects.get(LOGIN__id = lid)
        c = BookDoctorSerializer(data = request.data)
        
        if c.is_valid():
            c.save(USER=user,Status="Pending")
            return Response(c.data, status=HTTP_200_OK)
        
class BookingHistory(APIView):
    def get(self,request,lid):
        c = BookingTable.objects.filter(USER__LOGIN__id = lid)
        serializer = BookingHistorySerializer(c, many=True)
        print("----------------", serializer.data)
        return Response(serializer.data, status = HTTP_200_OK)

class ViewPrescriptionAPI(APIView):
    def get(self,request,id):
        c = Prescription.objects.filter(BOOKING = id)
        serializer = PrescriptionSerializer(c, many=True)
        print(serializer.data)
        return Response(serializer.data, status = HTTP_200_OK)
    
class ProfileView(APIView):
    def get(self,request,lid):
        c = UserTable.objects.get(LOGIN__id =lid)
        serializer = ProfileSerializer(c)
        return Response(serializer.data, status = HTTP_200_OK)
    def put(self,request,lid):
        user = UserTable.objects.get(LOGIN__id = lid)
        serializer = ProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.error, status=HTTP_400_BAD_REQUEST)

class FeedbackApi(APIView):
    def post(self, request, lid):
        print(request.data)
        try:
            c = UserTable.objects.get(LOGIN_id=lid)
        except UserTable.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        d = DoctorFeedbackSerializer(data=request.data)

        if d.is_valid():
            d.save(USER=c)
            return Response(d.data, status=status.HTTP_200_OK)
        else:
            return Response(d.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordApi(APIView):
    def post(self,request,lid):
        try:
            # Get user login record
            login_user = LoginTable.objects.get(id=lid)
        except LoginTable.DoesNotExist: 
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        if not all([old_password, new_password, confirm_password]):
            return Response({'error': 'All fields are required'}, status=HTTP_400_BAD_REQUEST)
        
        if login_user.Password != old_password:
            return Response({'error': 'Old password is incorrect'}, status=HTTP_400_BAD_REQUEST)
        
        if new_password != confirm_password:
            return Response({'error': 'New password and confirmation do not match'}, status=HTTP_400_BAD_REQUEST)
        
        login_user.Password = new_password
        login_user.save()

        return Response({'message': 'Password changed successfully'}, status=HTTP_200_OK)
            


    


        
