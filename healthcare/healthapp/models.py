from django.db import models

# Create your models here.
class LoginTable(models.Model):
    Username = models.CharField(max_length=30, blank=True, null=True)
    Password = models.CharField(max_length=30, blank=True, null=True)
    UserType = models.CharField(max_length=30,blank=True, null=True)

 
class HospitalTable(models.Model):
    UserName = models.CharField(max_length=30, blank=True, null=True)
    Registration_no = models.CharField(max_length=30, blank=True, null=True)
    E_mail = models.CharField(max_length=30, blank=True, null=True)
    Phone = models.BigIntegerField(blank=True, null=True)
    Address = models.CharField(max_length=100, blank=True, null=True)
    City = models.CharField(max_length=30, blank=True, null=True)
    State = models.CharField(max_length=30, blank=True, null=True)
    Pincode = models.IntegerField(blank=True, null=True)
    LOGIN = models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)

class UserTable(models.Model):
    UserName = models.CharField(max_length=30,blank=True, null=True)
    Gender = models.CharField(max_length=10, blank=True, null=True)
    DOB = models.DateField(blank=True,null=True)
    E_mail = models.CharField(max_length=30, blank=True, null=True)
    Phone = models.BigIntegerField(blank=True,null=True)
    Address = models.CharField(max_length=100,blank=True,null=True)
    City = models.CharField(max_length=30,blank=True,null=True)
    State = models.CharField(max_length=30,blank=True,null=True)
    Pincode = models.IntegerField(blank=True,null=True)
    LOGIN =models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    Created_at = models.DateTimeField(blank=True,null=True)


class DoctorTable(models.Model):
    UserName = models.CharField(max_length=30,blank=True,null=True)
    DOB = models.DateField(null=True,blank=True)
    Gender = models.CharField(max_length=10,blank=True,null=True)
    Specialization = models.CharField(max_length=80,blank=True,null=True)
    Qualification = models.CharField(max_length=80,blank=True,null=True)
    Experience_year = models.IntegerField(blank=True,null=True)
    E_mail = models.CharField(max_length=80,blank=True,null=True)
    Phone = models.BigIntegerField(blank=True,null=True)
    HOSPITAL = models.ForeignKey(HospitalTable,on_delete=models.CASCADE,blank=True,null=True)
    LOGIN = models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True,null=True)
    Added_on = models.DateTimeField(blank=True,null=True)


class FeedbackTable(models.Model):
    USER = models.ForeignKey(UserTable,on_delete=models.CASCADE,blank=True,null=True)
    DOCTOR = models.ForeignKey(DoctorTable,on_delete=models.CASCADE,blank=True,null=True)
    Rating = models.IntegerField(blank=True,null=True)
    Specialization = models.CharField(max_length=30,blank=True,null=True)
    Comment =  models.CharField(max_length=100,blank=True,null=True)
    Date = models.DateTimeField(blank=True,null=True)
    Status =  models.CharField(max_length=10,blank=True,null=True)

class ComplaintTbale(models.Model):
    USER = models.ForeignKey(UserTable,on_delete=models.CASCADE,blank=True,null=True)
    Against = models.CharField(max_length=30, blank=True,null=True)
    Subject =  models.CharField(max_length=100,blank=True,null=True)
    Description =  models.CharField(max_length=200,blank=True,null=True)
    Response = models.CharField(max_length=100,blank=True,null=True)
    Status = models.CharField(max_length=20,blank=True,null=True)

class ScheduleTable(models.Model):
    DOCTOR = models.ForeignKey(DoctorTable,on_delete=models.CASCADE,blank=True,null=True)
    Day_of_week = models.CharField(max_length=30,blank=True,null=True)
    Start_Time = models.DateTimeField(blank=True,null=True)
    End_Time = models.DateTimeField(blank=True,null=True)
    HOSPITAL = models.ForeignKey(HospitalTable,on_delete=models.CASCADE,blank=True,null=True)
    Status = models.CharField(max_length=10,blank=True,null=True)

class BookingTable(models.Model):
    USER = models.ForeignKey(UserTable,on_delete=models.CASCADE,blank=True,null=True)
    DOCTOR = models.ForeignKey(DoctorTable,on_delete=models.CASCADE,blank=True,null=True)
    Booking_date = models.DateField(blank=True,null=True)
    Booking_time = models.DateTimeField(blank=True,null=True)
    Status = models.CharField(max_length=20,blank=True,null=True)
    Payment_status = models.CharField(max_length=20,blank=True,null=True)
    Payment_mode = models.CharField(max_length=20,blank=True,null=True)
    Amount = models.FloatField(blank=True,null=True)
    Created_on = models.DateTimeField(blank=True,null=True)

class Prescription(models.Model):
    BOOKING = models.ForeignKey(BookingTable,on_delete=models.CASCADE,blank=True,null=True)
    USER = models.ForeignKey(UserTable,on_delete=models.CASCADE,blank=True,null=True)
    Date = models.DateField(blank=True,null=True)
    Diagnosis = models.CharField(max_length=100,blank=True,null=True)
    Advice = models.CharField(max_length=100,blank=True,null=True)
    Next_visit_date = models.DateField(blank=True,null=True)
    Created_on = models.DateTimeField(blank=True,null=True)
    
    
    
    








