from django.shortcuts import render
from rest_framework.response import Response;
from .serializers import DoctorSerializer;
from rest_framework.decorators import api_view
from .models import Doctor
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
    
    #  def get_object(self, pk):
    #     try:
    #         return DoctorSerializer.objects.get(pk=pk)
    #     except DoctorSerializer.DoesNotExist:
    #         pass

    
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
    
    def delete(self,request,format=None):
        id = request.GET.get('id')
        serializer = Doctor.objects.get(doctor_id=id)
        serializer.delete()
        return Response("Data Deleted Successfully...")