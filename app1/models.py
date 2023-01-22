from django.db import models

# Create your models here.
class Doctor (models.Model):
    doctor_name= models.CharField(max_length=25,blank=False)
    doctor_id= models.IntegerField(primary_key=True)
    description= models.CharField(max_length=500)
    def __str__(self) -> str:
        return f"{self.doctor_id} - {self.doctor_name}"


class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField(max_length = 200, null = True, blank = True)
    views = models.IntegerField()
    url = models.URLField(max_length = 200)
    # image = models.ImageField()