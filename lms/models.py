from django.db import models
from django.utils import timezone
class Leavemngt(models.Model):
	designation=models.CharField(max_length=50,default="0")
	uname=models.CharField(max_length=50,default="0")
	pwd=models.CharField(max_length=20,default="0")
	cpwd=models.CharField(max_length=20,default="0")
	class Meta:
		db_table="leavemngt"

class Leaveapply(models.Model):
	emp_name=models.CharField(max_length=100)
	l_type=models.CharField(max_length=100)
	l_days=models.CharField(max_length=100)
	l_from=models.DateField(max_length=30,default=timezone.now)
	l_to=models.DateField(max_length=30,default=timezone.now)
	l_status=models.CharField(max_length=100)
	class Meta:
		db_table="leaveapply"



