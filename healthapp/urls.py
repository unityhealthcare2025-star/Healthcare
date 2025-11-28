
from django.contrib import admin
from django.urls import path

from healthapp.views import *
from healthapp import views

urlpatterns = [
# //////////////////////////// ADMIN /////////////////////////////

    path('', LoginPage.as_view(), name="LoginPage"),
    path("AdminHome", AdminHome.as_view(), name="AdminHome"),
    path("VerifyHospital", VerifyHospital.as_view(), name="VerifyHospital"),
    path("AcceptHospital/<int:lid>", AcceptHospital.as_view(), name="AcceptHospital"),
    path("RejectHospital/<int:lid>",RejectHospital.as_view(), name="RejectHospital"),
    path("ViewDoctorRating", ViewDoctorRating.as_view(), name="ViewDoctorRating"),
    path("ViewUser", ViewUser.as_view(), name="ViewUser"),
    path("DeleteUser/<int:lid>", DeleteUser.as_view(), name="DeleteUser"),
 

#///////////////////////// HOSPITAL //////////////////////////////
   
   path("HospitalHome",HospitalHome.as_view(),name="HospitalHome"),
   path("Registration", Registration.as_view(), name="Registration"),
   path("ChangePassword", ChangePassword.as_view(), name="ChangePassword"),
   path("AddDoctor", AddDoctor.as_view(), name="AddDoctor"),
   path("ComplaintReply", ComplaintReply.as_view(), name="ComplaintReply"),
   path("CompReply/<int:c_id>", CompReply.as_view(), name="CompReply"),
   path("SearchComplaint", SearchComplaint.as_view(), name="SearchComplaint"),
   path("ManageDoctor", ManageDoctor.as_view(), name="ManageDoctor"),
   # path("Response", Response.as_view(), name="Response"),
   path("UpdateProfile", UpdateProfile.as_view(), name="UpdateProfile"),
   path("viewProfile", viewProfile.as_view(), name="viewProfile"),
   path('DeleteDoctor/<int:lid>/', DeleteDoctor.as_view(), name='DeleteDoctor'),
   path('EditDoctor/<int:doctor_id>/', EditDoctor.as_view(), name='EditDoctor'),
   path("EditDrProfile", EditDrProfile.as_view(), name="EditDrProfile"),
   path("ViewRating", ViewRating.as_view(), name="ViewRating"),
 
#/////////////////////////// DOCTOR /////////////////////////////

   path("DoctorHome",DoctorHome.as_view(),name="DoctorHome"),
   path("ManageSchedule",ManageSchedule.as_view(), name="ManageSchedule"),
   path("ViewBooking",ViewBooking.as_view(), name="ViewBooking"),
   path("UpdateDrProfile",UpdateDrProfile.as_view(), name="UpdateDrProfile"),
   path("viewDrProfile",viewDrProfile.as_view(), name="viewDrProfile"),
   path("ViewComplaints",ViewComplaints.as_view(), name="ViewComplaints"),
   path("ChangePassword1", ChangePassword1.as_view(), name="ChangePassword1"),
   path('DeleteSchedule/<int:lid>/', DeleteSchedule.as_view(), name='DeleteSchedule'),
   path("AddPrescription/<int:id>",AddPrescription.as_view(), name="AddPrescription"),




#/////////////////////USER///////////////////////////////////

path('userlogin', loginApiView.as_view(), name="userlogin"),
path('UserRegApiView',UserRegApiView.as_view(), name="UserRegApiView"),
path('nearby-hospitals', NearbyHospitalsAPIView.as_view(), name='nearby-hospitals'),
path('usersendComplaints/<int:id>',SendComplaintsApView.as_view(), name="usersendComplaints"),
# path('usersfeedback',FeedbackApiView.as_view(), name="usersfeedback"),
path('doctors-by-hospital/<int:hospital_id>', DoctorsByHospitalAPIView.as_view()),
path('doctorbooking/<int:id>', BookAppointmentAPIView.as_view()),
path('availability/<int:doctor_id>', DoctorAvailabilityView.as_view(), name='doctor-availability'),
path('bookdoctor/<int:lid>',BookDoctor.as_view(), name="bookdoctor"),
path('BookingHistory/<int:lid>',BookingHistory.as_view(), name="BookingHistory"),
path('ViewPrescription/<int:id>',ViewPrescriptionAPI.as_view(),name="ViewPrescription"),
path('ProfileView/<int:lid>',ProfileView.as_view(), name="ProfileView"),
path('Feedback/<int:lid>',FeedbackApi.as_view(), name="Feedback"),
path('ChangePassword/<int:lid>',ChangePasswordApi.as_view(), name="ChangePassword"),
path('accept_booking/<int:id>/', views.accept_booking, name='accept_booking'),
path('reject_booking/<int:id>/', views.reject_booking, name='reject_booking'),

]


