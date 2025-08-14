
from django.contrib import admin
from django.urls import path

from healthapp.views import *

urlpatterns = [
# //////////////////////////// ADMIN /////////////////////////////

    path('', LoginPage.as_view(), name="LoginPage"),
    path("AdminHome", AdminHome.as_view(), name="AdminHome"),
    path("VerifyHospital", VerifyHospital.as_view(), name="VerifyHospital"),
    path("ViewDoctorRating", ViewDoctorRating.as_view(), name="ViewDoctorRating"),
    path("ViewUser", ViewUser.as_view(), name="ViewUser"),
 

#///////////////////////// HOSPITAL //////////////////////////////
   
   path("HospitalHome",HospitalHome.as_view(),name="HospitalHome"),
   path("Registration", Registration.as_view(), name="Registration"),
   path("ChangePassword", ChangePassword.as_view(), name="ChangePassword"),
   path("AddDoctor", AddDoctor.as_view(), name="AddDoctor"),
   path("ComplaintReply", ComplaintReply.as_view(), name="ComplaintReply"),
   path("ManageDoctor", ManageDoctor.as_view(), name="ManageDoctor"),
   path("Response", Response.as_view(), name="Response"),
   path("UpdateProfile", UpdateProfile.as_view(), name="UpdateProfile"),
   
#/////////////////////////// DOCTOR /////////////////////////////

   path("DoctorHome",DoctorHome.as_view(),name="DoctorHome"),
   path("ManageSchedule",ManageSchedule.as_view(), name="ManageSchedule"),
   path("ViewBooking",ViewBooking.as_view(), name="ViewBooking"),
   path("Updateprofile",Updateprofile.as_view(), name="Updateprofile"),
   path("ViewComplaints",ViewComplaints.as_view(), name="ViewComplaints")
   
   
]