from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Doctor
        # fields = ('doctor_id','doctor_name','description')
        fields = '__all__'