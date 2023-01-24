from django.shortcuts import render
from rest_framework.response import Response;
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer;
from rest_framework.decorators import api_view
from .models import Doctor, Patient_Registration, Appointment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# Create your views here.


def front(request):
    context = {}
    return render(request, "index.html", context)


    

# @api_view(['GET', 'POST','DELETE'])
# def doctorsList(request,id):
#     if request.method == 'GET':
#         doctors = Doctor.objects.all()
#         serializer = DoctorSerializer(doctors, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = DoctorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         serializer = DoctorSerializer.objects.get(doctor_id=id)
#         serializer.delete()
#         return Response("Data Deleted Successfully...")

# @api_view(['POST'])
    """_summary_
    """# def adddoctorsList(request):
    
    
class doctorsList(APIView):
    def get_object(self, id):
        try:
            return Doctor.objects.get(doctor_id=id)
        except Doctor.DoesNotExist:
            raise Http404
        
    def get(self,request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        # return Response(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,*args, **kwargs):
        id = request.GET['id']
        print("============================")
        print("The doctor's id is = ",id)
        print("============================")
        # id = request.GET.get('id')
        # serializer = Doctor.objects.get(doctor_id=id)
        serializer = self.get_object(id)
        serializer.delete()
        return Response("Data Deleted Successfully...")
    
    
class Patient_list(APIView):
    def get_object(self, id):
        try:
            return Patient_Registration.objects.get(patient_id=id)
        except Patient_Registration.DoesNotExist:
            raise Http404
        
    def get(self,request):
        patients = Patient_Registration.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        # return Response(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,format=None):
        id = request.GET['id']
        print("============================")
        print("The id is = ",id)
        print("============================")
        # id = request.GET.get('id')
        # serializer = Doctor.objects.get(doctor_id=id)
        serializer = self.get_object(id)
        serializer.delete()
        return Response("Data Deleted Successfully...")
    
       
class Appointment_list(APIView):
    def get_object(self, id):
        try:
            return Appointment.objects.get(appointment_id=id)
        except Appointment.DoesNotExist:
            raise Http404
    def get(self,request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        # return Response(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,format=None):
        id = request.GET['id']
        print("============================")
        print("The appointment id is = ",id)
        print("============================")
        # id = request.GET.get('id')
        # serializer = Doctor.objects.get(doctor_id=id)
        serializer = self.get_object(id)
        serializer.delete()
        return Response("Data Deleted Successfully...")
    