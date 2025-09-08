from rest_framework import serializers

from healthapp.models import BookingTable, ComplaintTable, DoctorTable, FeedbackTable, HospitalTable, UserTable
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserTable
        fields=['UserName','Gender','DOB','E_mail','Phone','Address',' City','State',' Pincode']

class DoctorFeedbackSerializer(serializers.ModelSerializer):      
     class Meta:
        model=FeedbackTable
        fields=['DOCTOR ','Rating','Comment']

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model=ComplaintTable
        fields=['Subject','Description']

class ViewHospitalSerializeclass(serializers.ModelSerializer):
     class Meta:
        model=HospitalTable
        fields=['City','Pincode']

class ViewDoctorSerializeclass(serializers.ModelSerializer):
     class Meta:
        model=DoctorTable
        fields=['HOSPITAL']

class BookingSerializeclass(serializers.ModelSerializer):
     class Meta:
        model=BookingTable
        fields=['DOCTOR','Booking_date','Booking_time']

class EditProfileSerializer(serializers.ModelSerializer):
     class Meta:
        model=UserTable
        fields=['UserName','E_mail','Phone','DOB','Gender','Address']


         
