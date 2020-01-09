from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns=[
    path('',TemplateView.as_view(template_name='index.html'),name='admin'),
    path('login/',TemplateView.as_view(template_name='login.html'),name='login'),
    
    path('admin',views.authentication,name='admin_login'),
    path('add_faculty',TemplateView.as_view(template_name='addfact.html'),name='addfaculty' ),

    path('addfaculty',views.addfaculty,name='addfact'),
    path('facultyRegistration',TemplateView.as_view(template_name='faculty.html'),name='faculty'),
    path('studentregistration',TemplateView.as_view(template_name='studentregistration.html'),name='studentregistration' ),


    path('facultysignup',views.factsign,name='facultysignup'),
    path('studentsignup',views.signupstud,name='studregistration'),
    path('studentattantance',views.studattan,name='stdattantance'),
    path('stuleave/',views.stdleave,name='studentleave'),
    path('faculeave/',views.facleave,name='facultyleave'),



    path('smark/',views.studmark,name='studentmark'),
    path('mydetails/',TemplateView.as_view(template_name='personaldetails.html'),name='personaldetails'),
    path('details/',views.detailsstudent,name='personaldetails'),
    path('markdetail/',TemplateView.as_view(template_name='viewmark.html'),name='viewmark'),
    path('markdetails/',views.markview,name='viewmark'),

    path('attantancedetails/',TemplateView.as_view(template_name='viewattantance.html'),name='viewattantance'),
    path('attantancedetail',views.attantanceview,name='viewattantance'),

    path('mystud/',TemplateView.as_view(template_name='viewstudt.html'),name='viewstud'),
    path('studentdetails/',views.studview,name='view_stud'),

    path('myfac/',TemplateView.as_view(template_name='viewfac.html'),name='view'),
    path('',TemplateView.as_view(template_name='logout.html'),name='logout'),
    path('facdetails/',views.facview,name='view_fac'),


      ]