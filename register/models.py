from django.db import models
# Create your models here.
class admin(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
class faculty(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    password=models.CharField(max_length=20,null=True,blank=True)
class meta:
    db_table:"register_faculty"
class facultysignup(models.Model):
    factid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    dob=models.DateField(max_length=10)
    gender=models.CharField(max_length=10)
    qualification=models.CharField(max_length=20)
    mobile=models.IntegerField(null=True,blank=True)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    assbatch=models.CharField(max_length=20)
    class meta:
        db_table:"register_facultysignup"
class student(models.Model):
    stdid=models.IntegerField(primary_key=True)
    admno=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    dob=models.DateField(max_length=10)
    gender=models.CharField(max_length=10)
    mobile=models.IntegerField(null=True,blank=True)
    admdate=models.DateField(max_length=10)
    guardian=models.CharField(max_length=30)
    batch=models.CharField(max_length=30)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
class meta:
        db_table:"register_student"
class studentattend(models.Model):
    date=models.DateField(max_length=10)
    stdid=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=30)
    hour1status=models.CharField(max_length=30)
    hour2status=models.CharField(max_length=30)
    hour3status=models.CharField(max_length=30)
    hour4status=models.CharField(max_length=30)
class meta:
        db_table:"register_studentattend"
class facleave(models.Model):
    name=models.CharField(max_length=30)
    reason=models.CharField(max_length=30)
    fromdate=models.DateField(max_length=10)
    todate=models.DateField(max_length=10)
class meta:
        db_table:"register_facleave"   
class studleave(models.Model):
    name=models.CharField(max_length=30)
    reason=models.CharField(max_length=30)
    fromdate=models.DateField(max_length=10)
    todate=models.DateField(max_length=10)
class meta:
        db_table:"register_studleave" 
class studentmark(models.Model):
    stdid=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=30)
    assessmentno=models.IntegerField(null=True,blank=True)
    sub1mark=models.IntegerField(null=True,blank=True)
    sub2mark=models.IntegerField(null=True,blank=True)
    sub3mark=models.IntegerField(null=True,blank=True)
    percentage=models.IntegerField(null=True,blank=True)
class meta:
        db_table:"register_studentmark"
 
