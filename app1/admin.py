from django.contrib import admin
from app1.models import Doctor, GeeksModel

# @admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Doctor),
admin.site.register(GeeksModel)