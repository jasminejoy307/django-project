from django.urls import path
from register import views
from django.views.generic import TemplateView
urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('admin/',TemplateView.as_view(template_name='admin.html'),name='admin'),
    path('addfaculty/',TemplateView.as_view(template_name='addfaculty.html'),name='addfaculty'),
    path('index',views.authentication,name='submit'),
    path('addfaculty',views.addfaculty,name='addfaculty'),
    path('facultyregistration/',TemplateView.as_view(template_name='faculty.html'),name='faculty'),
    path('studentregistration/',TemplateView.as_view(template_name='studentreg.html'),name='studentreg'),
    path('facultysignup/',views.facultysign,name='facultysignup'),
    path('studentsignup/',views.signupstud,name='studregistration'),
    path('studattendn/',views.studattend,name='studentattendence'),
    path('facleaveapply/',views.facultyleave,name='facapplyleave'),
    path('studleaveapply/',views.studentleave,name='studapplyleave'),
    path('stumark/',views.studmark,name='studentmark'),
    path('password/',TemplateView.as_view(template_name='passwordchange.html'),name='passwordchange'),
    path('mobile/',TemplateView.as_view(template_name='mobilechange.html'),name='mobilechange'),
    path('email/',TemplateView.as_view(template_name='emailchange.html'),name='emailchange'),
    path('mydetails/',TemplateView.as_view(template_name='personaldetails.html'),name='personaldetails'),
    path('details/',views.detailsstudent,name='personaldetails'),
    path('mymarks/',TemplateView.as_view(template_name='viewmark.html'),name='viewmark'),
    path('markdetails/',views.markview,name='viewmark'),
    path('myattendence/',TemplateView.as_view(template_name='myattend.html'),name='myattend'),
    path('attendencedetails/',views.attendview,name='myattend'),
    path('myfac/',TemplateView.as_view(template_name='viewfac.html'),name='view'),
    path('facdetails/',views.facview,name='view'),
    path('mystud/',TemplateView.as_view(template_name='viewstud.html'),name='viewstud'),
    path('studentdetails/',views.studview,name='viewstud'),
    path('',TemplateView.as_view(template_name='logout.html'),name='logout'),
   
    
    

]
