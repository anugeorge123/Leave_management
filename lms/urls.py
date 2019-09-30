from django.urls import path
from . import views

urlpatterns = [
    path('',views.method1,name='firstpage1'),
	
	path('signup1/',views.signup1,name='sign up'),
	
	path('signup1/signup/',views.signup,name='Sign up'),
	
	path('leaveapply/',views.leaveapply,name='Leave application'),
	path('leaveapply/leaveapplyfn/',views.checkfn,name='Leave application'),
	path('loginfn/',views.managerlogin,name='First Page of The HTML'),
	path('currentleave/',views.currentleave,name='current leave apllications'),
	path('currentleave/currentleavefn/',views.currentleavefn,name='current leave apllications'),
	path('currentleave/selectfn/',views.selectfn,name='select'),
		
	path('currentleave/approve/',views.approve,name='manager approval'),
	path('currentleave/reject/',views.reject,name='manager reject'),
	path('leaveapply/viewleave/',views.viewleave,name='view approved leave'),
	
	path('leaveapply/viewleavefn/',views.viewleavefn,name='view approved leave'),
	
	
	
	
]
