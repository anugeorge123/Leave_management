from django.shortcuts import render
from lms.models import Leaveapply
from lms.models import Leavemngt
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,authenticate
from django.contrib.auth.hashers import check_password
import datetime 
from datetime import date 
import calendar 

import json

def method1(request):
	return render(request,"firstpage1.html")

def leaveapply(request):
	return render(request,"leaveapply.html")

def checkfn(request):
	dic1={}
	from_date=request.POST['date_from']
	to_date=request.POST['date_to']
	today = date.today()
	d1 = today.strftime("%d/%m/%Y")
	print("d1 =", d1)
		
	print("from date",from_date)
	print("to date",to_date)
	
	if(from_date >=d1 and to_date>=d1):
		dic1=leaveapplyfn(request)
		
	else:
		print("error")
		dic1["status"]=False

	jsondata=json.dumps(dic1)
	return HttpResponse(jsondata,content_type="application/json")

	
def leaveapplyfn(request):
	dict2={}
	name=request.POST['txt_name']
	ltype=request.POST['txt_leave']
	day=int(request.POST['txt_day'])
	from_date=request.POST['date_from']
	to_date=request.POST['date_to']

	print(name,ltype,day)
	try:
		if(ltype=='sick leave' ):
			if(day<=12):
				
				try:
					select = Leaveapply.objects.get(emp_name = name,l_type=ltype)
					
				except Exception as e:
					select=None
				if(select==None):
					x=Leaveapply(emp_name=name,l_type=ltype,l_days=day,l_from=from_date,l_to=to_date,l_status='0')
					x.save()
					
					dict2["val1"]=name+" : "+ltype+" :"+str(day)
					dict2["val2"]=ltype
					dict2["val3"]=int(day)

					dict2["status"]=True
					print(dict2)
				else:
					objects = Leaveapply.objects.get(emp_name=name,l_type=ltype)
					dayy=int(objects.l_days)
					print("dayy",dayy)
					dayy=dayy+day
								
					objects.l_days = dayy
					
					if(name !="" and ltype != "" and dayy !="" and dayy<=12):
						objects.save()

					
					dict2["val1"]=name+" : "+ltype+" :"+str(dayy)
					dict2["val2"]=ltype
					dict2["val3"]=int(dayy)
					dict2["status"]=True
				

	
		if(ltype=='annual leave'):
			request.session["key1"]=name
			request.session["key2"]=ltype
			request.session["key3"]=day
			request.session["key4"]=from_date
			request.session["key5"]=to_date
			dic=annualleavefn(request)
			print("dictionary aftr rtrn:",dic)
			print("val3------>",dic["val1"])

			#dict2["val1"]
			dict2["status"]=True
		if(ltype=='marriage leave'):
			if(day<=5):
				try:
					select = Leaveapply.objects.get(emp_name = name,l_type=ltype)
					
				except Exception as e:
					select=None
				if(select==None):
					x=Leaveapply(emp_name=name,l_type=ltype,l_days=day,l_from=from_date,l_to=to_date,l_status='1')
					x.save()
					
					dict2["val1"]=name+" : "+ltype+" :"+str(day)
					dict2["val2"]=ltype
					dict2["val3"]=int(day)
					dict2["status"]=True
				else:
					objects = Leaveapply.objects.get(emp_name=name,l_type=ltype)
					dayy=int(objects.l_days)
					print("dayy",dayy)
					dayy=dayy+day
								
					objects.l_days = dayy
					
					if(name !="" and ltype != "" and dayy !="" and dayy<=5):
						objects.save()
										
					dict2["val1"]=name+" : "+ltype+" :"+str(dayy)
					dict2["val2"]=ltype
					dict2["val3"]=int(dayy)
					dict2["status"]=True
								
		if(ltype=='maternity leave'):
			if(day<=30):
				try:
					select = Leaveapply.objects.get(emp_name = name,l_type=ltype)
					
				except Exception as e:
					select=None
				if(select==None):
					x=Leaveapply(emp_name=name,l_type=ltype,l_days=day,l_from=from_date,l_to=to_date,l_status='1')
					x.save()
					
					dict2["val1"]=name+" : "+ltype+" :"+str(day)
					dict2["val2"]=ltype
					dict2["val3"]=int(day)
					dict2["status"]=True
				else:
					objects = Leaveapply.objects.get(emp_name=name,l_type=ltype)
					dayy=int(objects.l_days)
					print("dayy",dayy)
					dayy=dayy+day
								
					objects.l_days = dayy
					
					if(name !="" and ltype =="maternity leave" and dayy !="" and dayy<=30):
						objects.save()
					objects.l_type = ltype
					objects.emp_name = name
									
					if(name !="" and ltype !="maternity leave" and dayy !="" and dayy<=30):
						objects.save()

										
					dict2["val1"]=name+" : "+ltype+" :"+str(dayy)
					dict2["val2"]=ltype
					dict2["val3"]=int(dayy)
					dict2["status"]=True
		

	except Exception as e:
		print(e)			
		dict2["status"]=False
	
	return dict2
	

def annualleavefn(request):
	dict2={}

	name=request.session["key1"]

	#print("annual fn---->",name)
	ltype=request.session["key2"]
	day=request.session["key3"]
	from_date=request.session["key4"]
	to_date=request.session["key5"]	


	
	try:	
		if(day<=12):
			year, month, date = (int(i) for i in from_date.split('-'))
			dayNumber = calendar.weekday(year, month, date)
			year1, month1, date1 = (int(i) for i in to_date.split('-'))
			dayNumber1 = calendar.weekday(year1, month1, date1)		
			days =["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]
			f_day=days[dayNumber]
			t_day=days[dayNumber1]
			print(f_day,"---->",t_day) 
			try:
				select = Leaveapply.objects.get(emp_name = name,l_type=ltype)
			except Exception as e:
				select=None
				print("1 except")
			if(select==None):
				if(f_day=="Monday" or t_day=="Monday"):
					day=day+2
					x=Leaveapply(emp_name=name,l_type=ltype,l_days=day,l_from=from_date,l_to=to_date,l_status='1')
					x.save()
					dict2["val1"]=name+" : "+ltype+" :"+str(day)
					#dict2["val2"]=ltype
					#dict2["val3"]=int(day)
					#dict2["status"]=True
				else:

					x=Leaveapply(emp_name=name,l_type=ltype,l_days=day,l_from=from_date,l_to=to_date,l_status='1')
					x.save()
					dict2["val1"]=name+" : "+ltype+" :"+str(day)
					#dict2["val2"]=ltype
					#dict2["val3"]=int(day)
					#dict2["status"]=True

			else:
				objects = Leaveapply.objects.get(emp_name=name,l_type=ltype)
				dayy=int(objects.l_days)
				print("dayy",dayy)
				#dayy=dayy+day
				if(f_day=="Monday" or t_day=="Monday"):
					day=day+2
					objects.l_days = dayy+day
					if(name !="" and ltype != "" and dayy !="" and dayy<=12):
						objects.save()
						dict2["val1"]=name+" : "+ltype+" :"+str(dayy)
						dict2["val2"]=ltype
						dict2["val3"]=str(dayy)
		print("dict2--------->",dict2)
		return dict2
		
	except Exception as e:
		print(e)	


	
		
def managerlogin(request):
	dict3={}
	uname = request.POST['txt_uname']
	pwd=request.POST['txt_pwd']
		
	#print(uname,"--->",pwd)
	select=''
	try:
		obj3=User.objects.get(username=uname)
		groupId=obj3.groups.get()
		groupName=Group.objects.get(id=groupId.id)
		#print(obj3.username," -> ",groupName.name)
		select += obj3.username+" : "+obj3.password+" \n"
		#print("query",select)
		print(obj3.username," ---> ",obj3.password)

		#matchcheck= check_password(pwd, obj3.password)
		auth=authenticate(request,username=uname,password=pwd)
		if(auth is not None):
		#if matchcheck:
			login(request,auth)
			if(groupName.name=="manager"):
				dict3["val1"]="manager"
				print("hello")
			elif(groupName.name=="employee"):
				dict3["val2"]="employee"
				print("haiii")
		
		else:
			dict3["val3"]="Wrong Password"
		dict3["status"]=True
	except Exception as e:
		print(e)
		dict3["status"]=False
		
	print(dict3)
	jsondata=json.dumps(dict3)
	return HttpResponse(jsondata,content_type="application/json")
	
			
def currentleave(request):
	return render(request,"currentleave.html")


def currentleavefn(request):
	dict4={}
	try:
		
		objects = Leaveapply.objects.filter(l_status="1")
		lis_name=set()	
		lis_type=list()
		lis_days=list()
		lis_fdate=list()
		lis_todate=list()
		for x in objects:
			#lis.append("<option>"+x.emp_name+"</option>")
			lis_name.add(x.emp_name)
			lis_type.append(x.l_type)
			lis_days.append(x.l_days)
			lis_fdate.append(str(x.l_from))
			lis_todate.append(str(x.l_to))
		
		print(lis_name,lis_type,lis_fdate)
		dict4["val1"]=list(lis_name)
		dict4["val3"]=lis_type
		dict4["val4"]=lis_days	
		dict4["val5"]=lis_fdate
		dict4["val6"]=lis_todate	
		#dict4["val4"]=x.l_days

		dict4["val2"]=len(lis_name)
		dict4["status"]=True
		print(dict4)
	except Exception as e:
		print("Current Leave Fn:",e)
		dict4["status"]=False
		
	jsondata=json.dumps(dict4)
	return HttpResponse(jsondata,content_type="application/json")


def selectfn(request):
	dic={}
	try:
		print("haiii")
		print("select fn")
		print(request.POST)
		sel=request.POST['select']
		print("select -->",sel)

		x = Leaveapply.objects.filter(emp_name=sel,l_status="1")		
		dic["val1"]=x[0].emp_name
		dic["val2"]=x[0].l_type
		dic["val3"]=x[0].l_days
		dic["val4"]=str(x[0].l_from)
		dic["val5"]=str(x[0].l_to)
		dic["status"]=True
	except Exception as e:
		dic["status"]=False 
		print(e)
	jsondata=json.dumps(dic)
	return HttpResponse(jsondata,content_type="application/json")
'''
#currentleavefn using text box
def currentleavefn(request):
	dict4={}
	try:
		st="1"
		leaveObj = Leaveapply.objects.filter(l_status=st)
		
		select=''	
		for x in leaveObj:
			select=select+x.emp_name+"   "+x.l_type+"   "+x.l_days+" \n"
		print(select)
		dict4["val1"]=select
		dict4["val2"]=x.emp_name
		dict4["val3"]=x.l_type
		dict4["val4"]=x.l_days
		dict4["status"]=True
		print(dict4)
	except Exception as e:
		print("Current Leave Fn:",e)
		dict4["status"]=False
		
	jsondata=json.dumps(dict4)
	return HttpResponse(jsondata,content_type="application/json")


'''

def approve(request):
	dict5={}
	try:
		print("inside approve")
		print(request.POST)
		empname=request.POST['select']
		print("employee: ",empname)

		try:
			print("inside try")
			select = Leaveapply.objects.filter(emp_name = empname,l_status="1")
			print("haii",select[0].l_status)
		except Exception as e:
			select=None
		if(select!=None):
			obj=select[0]
			status=obj.l_status
			print("sts",status)
			print("Employee->",obj.emp_name)
			if(status=='1'):
				obj.l_status="2"
				obj.save()
				dict5["status"]=True
				print("Leave Status->",obj.l_status)
	except Exception as e:
		print("approve function->",e)
		dict5["status"]=False
	print(dict5)
	jsondata=json.dumps(dict5)
	return HttpResponse(jsondata,content_type="application/json")


def reject(request):
	dict5={}
	try:
		empname=request.POST['select']	
		print(empname)
		try:
			select = Leaveapply.objects.filter(emp_name = empname,l_status="1")
		except Exception as e:
			select=None
		if(select!=None):
			obj=select[0]
			status=obj.l_status
			#objects = Leaveapply.objects.get(emp_name=empname)
			#status=objects.l_status
			if(status=='1'):
				obj.l_status ='3'
				obj.save()
				dict5["status"]=True
	except Exception as e:
		print("reject function->",e)
		dict5["status"]=False
	print(dict5)
	jsondata=json.dumps(dict5)
	return HttpResponse(jsondata,content_type="application/json")


def viewleave(request):
	return render(request,"viewapprovedleave.html")
	

	
def viewleavefn(request):
	dict6={}
		
	try:
		st="2"
		objects = Leaveapply.objects.filter(l_status=st)
		
		select ='            APPROVED LEAVE        \n\nName		Leavetype		No.of Days\n\n'
		print("hai")
		for x in objects:
			select =select+ x.emp_name+"		"+x.l_type+"		"+x.l_days+" \n"
		
		print("view approved",select)
		dict6["val"]=select
		dict6["status"]=True
	except Exception as e:
		print("view leave fn",e)
		dict6["status"]=False
		print(dict6)
	jsondata=json.dumps(dict6)
	return HttpResponse(jsondata,content_type="application/json")




def signup1(request):
	return render(request,"login.html")


def signup(request):
	dict6={}
	try:
		designation=request.POST['txt_des']
		#request.session['key1']=designation	
		uname=request.POST['txt_uname']	
		pwd=request.POST['txt_pwd']
		cpwd=request.POST['txt_pwd']
		print("confirm pwd: ",cpwd)	
		
		if(pwd==cpwd):
			
			x=User.objects.create_user(is_superuser="0",username=uname,password=pwd)
			x.save()

		
		if(designation=="manager"):
			u=User.objects.get(username=uname)
			g=Group.objects.get(name='manager')
			u.groups.add(g)
			u.save()
		if(designation=="employee"):
			u=User.objects.get(username=uname)
			g=Group.objects.get(name='employee')
			u.groups.add(g)
			u.save()
		dict6["status"]=True
	except Exception as e:
		print("approve function->",e)
		dict6["status"]=False
	print(dict6)
	jsondata=json.dumps(dict6)
	return HttpResponse(jsondata,content_type="application/json")
