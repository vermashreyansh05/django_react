from django.contrib import admin
from django.urls import path
from .views import front,doctorsList
urlpatterns = [
       path("/main", front, name="front"),
       path("", front, name="front"),
       path('doctors_list', doctorsList.as_view(), name='doc_list'),
       path('doctors_list/<int:id>/', doctorsList.as_view(), name='doc_list'),
       # path('doctors_list', adddoctorsList, name='add_doc_list'),
]