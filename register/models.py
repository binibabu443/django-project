from django.db import models
class admin(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=20)

class faculty(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=20)

class meta:
    db_table:"faculty"
    
class meta:
    db_table:"register_faculty"
    

class facultysignup(models.Model):
    factid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    dob=models.DateField(max_length=10)
    gender=models.CharField(max_length=30)
    qualification=models.CharField(max_length=30)
    mobile=models.IntegerField(null=True,blank=True)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=10)
    assbatch=models.CharField(max_length=10)

class student(models.Model):
    sid=models.IntegerField(primary_key=True)
    admno=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    dob=models.DateField(max_length=10)
    gender=models.CharField(max_length=30)
    mobile=models.IntegerField(null=True,blank=True)
    admdate=models.DateField(max_length=10)
    guardian=models.CharField(max_length=30)
    batch=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=10)
class meta:
    db_table:"register_student"
    db_table:"register_studentattantance"

"""class facultyattentance(models.Model):
    factid=models.ForeignKey(faculty,related_name='factid',on_delete=models.PROTECT)
    name=models.CharField(max_length=30)
    id=models.IntegerField(max_length=30,unique=True)
    date=models.DateField(max_length=10)
    hours1status=models.CharField(max_length=5)
    hours2status=models.CharField(max_length=5)
    hours3status=models.CharField(max_length=5)
    hours4status=models.CharField(max_length=5)"""

class studentattantance(models.Model):
    date=models.DateField(max_length=10)
    sid=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=30)
    hours1status=models.CharField(max_length=15)
    hours2status=models.CharField(max_length=15)
    hours3status=models.CharField(max_length=15)
    hours4status=models.CharField(max_length=15)
    class meta:
        db_table:"register_studentattantance"

class sleave(models.Model):
    name=models.CharField(max_length=30)
    fromdate=models.DateField(max_length=10)
    todate=models.DateField(max_length=10)
    reason=models.CharField(max_length=30)
    class meta:
        db_table:"register_sleave"


class fleave(models.Model):
    name=models.CharField(max_length=30)
    fromdate=models.DateField(max_length=10)
    todate=models.DateField(max_length=10)
    reason=models.CharField(max_length=30)
    class meta:
        db_table:"register_fleave"


class studentmark(models.Model):
    sid=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=30)
    assessmentno=models.IntegerField(null=True,blank=True)
    sub1mark=models.IntegerField(null=True,blank=True)
    sub2mark=models.IntegerField(null=True,blank=True)
    sub3mark=models.IntegerField(null=True,blank=True)
    percentage=models.IntegerField(null=True,blank=True)
    class meta:
        db_table:"register_studentmark"
 
    









