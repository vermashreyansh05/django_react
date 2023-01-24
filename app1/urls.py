from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import front,doctorsList,Patient_list,Appointment_list
urlpatterns = [
       path("main", front, name="front"),
       path("", front, name="front"),
       path('doctors_list', doctorsList.as_view(), name='doc_list'),
       path('doctors_list/<int:id>', doctorsList.as_view(), name='doc_list'),
       path('patient_list', Patient_list.as_view(), name='patient_list'),
       path('patient_list/<int:id>/', Patient_list.as_view(), name='patient_list'),
        path('appointment_list', Appointment_list.as_view(), name='appointment_list'),
       path('appointment_list/<int:id>/', Appointment_list.as_view(), name='appointment_list'),
       # path('doctors_list', adddoctorsList, name='add_doc_list'),
]