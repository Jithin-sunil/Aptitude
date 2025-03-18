from django.db import models




# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=40)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=40)

class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=40)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    
class tbl_adminreg(models.Model):
    admin_name=models.CharField(max_length=40)
    admin_email=models.CharField(max_length=50)
    admin_pass=models.CharField(max_length=40)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=40)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_subject(models.Model):
    subject_name=models.CharField(max_length=40)

class tbl_level(models.Model):
    level_name=models.CharField(max_length=40)
    time_limit = models.IntegerField(default=30,null=True)

