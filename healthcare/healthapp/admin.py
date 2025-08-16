from django.contrib import admin

from healthapp.models import *

# Register your models here.
admin.site.register(LoginTable)
admin.site.register(HospitalTable)
admin.site.register(UserTable)
admin.site.register( DoctorTable)
admin.site.register(FeedbackTable)
admin.site.register(ComplaintTable)
admin.site.register(ScheduleTable)
admin.site.register(BookingTable)
admin.site.register(Prescription)