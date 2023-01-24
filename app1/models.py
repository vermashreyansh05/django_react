from django.db import models

# Create your models here.
class Doctor (models.Model):
    doctor_name= models.CharField(max_length=25,blank=False)
    doctor_id= models.IntegerField(primary_key=True)
    description= models.CharField(max_length=500)
    def __str__(self) -> str:
        return f"{self.doctor_id} - {self.doctor_name}"


class Appointment(models.Model):
    appointment_id = models.IntegerField(primary_key=True)
    doctor_id = models.ForeignKey("Doctor", on_delete=models.CASCADE)
    patient_id = models.ForeignKey("Patient_Registration", on_delete=models.CASCADE)
    # image = models.ImageField()
    def __str__(self) -> str:
        return f"{self.appointment_id} - {self.appointment_of} - {self.appointment_with}"
    
class Patient_Registration(models.Model):
    patient_id = models.IntegerField(primary_key=True, default=0)
    username = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20, )
    lastname = models.CharField(max_length=20,null=True,blank=True)
    email = models.EmailField()
    mobile = models.CharField(max_length=10,null=True,blank=True)
    city = models.CharField(max_length=10,null=True,blank=True)
    country = models.CharField(max_length=10,null=True,blank=True)
    pswrd= models.CharField( max_length=50)
    usertype = models.CharField( max_length=20)
    def __str__(self) -> str:
        return f'{self.firstname} -  {self.lastname}'
    
