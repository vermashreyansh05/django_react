from django.contrib import admin
from app1.models import Doctor, Patient_Registration, Appointment

# @admin.register(Doctor)
# class DoctorAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Doctor),
admin.site.register(Patient_Registration),
admin.site.register(Appointment),
# admin.site.register(GeeksModel)