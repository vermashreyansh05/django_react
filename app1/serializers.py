from rest_framework import serializers
from .models import Doctor, Patient_Registration, Appointment

class DoctorSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Doctor
        # fields = ('doctor_id','doctor_name','description')
        fields = '__all__'
        
class PatientSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Patient_Registration
        # fields = ('doctor_id','doctor_name','description')
        fields = '__all__'
        
class AppointmentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Appointment
        # fields = ('doctor_id','doctor_name','description')
        fields = '__all__'