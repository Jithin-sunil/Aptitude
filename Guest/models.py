from django.db import models
from Admin.models import *  

# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=40)
    user_contact=models.CharField(max_length=10)
    user_email=models.CharField(max_length=40)
    user_pass=models.CharField(max_length=10)
    user_address=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_photo=models.FileField(upload_to="Assest/File/User/")

class tbl_master(models.Model):
    master_name=models.CharField(max_length=40)
    master_contact=models.CharField(max_length=10)
    master_email=models.CharField(max_length=40)
    master_pass=models.CharField(max_length=10)
    master_address=models.CharField(max_length=50)
    master_proof=models.FileField(upload_to="Assest/File/master/")
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    master_photo=models.FileField(upload_to="Assest/File/master/")
    master_vstatus=models.IntegerField(default=0)
