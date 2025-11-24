from rest_framework import serializers

from healthapp.models import *
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserTable
        fields=['UserName','Gender','DOB','E_mail','Phone','Address','City','State','Pincode']

class DoctorFeedbackSerializer(serializers.ModelSerializer):      
     class Meta:
        model=FeedbackTable
        fields=['DOCTOR ','Rating','Comment']

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model=ComplaintTable
        fields=['Subject','Description','HOSPITAL','Response']

class ViewHospitalSerializeclass(serializers.ModelSerializer):
     class Meta:
        model=HospitalTable
        fields=['City','Pincode']

class ViewDoctorSerializeclass(serializers.ModelSerializer):
     class Meta:
        model=DoctorTable
        fields=['HOSPITAL']

class BookingSerializer(serializers.ModelSerializer):
     class Meta:
        model=BookingTable
        fields=['DOCTOR','Booking_date','Booking_time','Status','Payment_status','Payment_mode',
        'Amount']

class EditProfileSerializer(serializers.ModelSerializer):
     class Meta:
        model=UserTable
        fields=['UserName','E_mail','Phone','DOB','Gender','Address']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=LoginTable
        fields=['Username','Password','UserType']
         

class SchedulSerailizer(serializers.ModelSerializer):
    class Meta:
        model=ScheduleTable
        fields='__all__'

class BookDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        fields = ['SCHEDULEID', 'Booking_date']

class BookingHistorySerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='USER.UserName')
    doctor_name = serializers.CharField(source='SCHEDULEID.DOCTOR.UserName')
    doctor_id = serializers.CharField(source='SCHEDULEID.DOCTOR.id')
    schedule_day = serializers.CharField(source='SCHEDULEID.Day_of_week')
    Start_Time = serializers.TimeField(source='SCHEDULEID.Start_Time')
    End_Time = serializers.TimeField(source='SCHEDULEID.End_Time')
    

    bookingid = serializers.IntegerField(source='id')
    class Meta:
        model = BookingTable
        fields = ['id','Status','Start_Time','End_Time','Created_on','user_name', 'doctor_name', 'schedule_day', 'Booking_date', 'bookingid', 'doctor_id']

        
class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
     class Meta:
        model =  UserTable
        fields = '__all__'
