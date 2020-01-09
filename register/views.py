from django.shortcuts import render
from django.http import HttpResponse
from register.models import admin,faculty,facultysignup,student,studentattantance,sleave,studentmark,fleave

def authentication (request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        username=str(username)
        password=str(password)
        u=admin.objects.filter(username=username)
        p=admin.objects.filter(password=password)
        c=0
        if u.count()==1 and p.count()==1:
            c+=1
            return render(request,'admin.html')
        else:
            u1=faculty.objects.filter(username=username)
            p1=faculty.objects.filter(password=password)
            if u1.count()==1 and p1.count()==1:
                return render(request,'factpage.html')


            else:
                u=student.objects.filter(name=username,password=password)
                if u.count()==1:
                    request.session['usernm']=username
                    qry=student.objects.all().filter(name=username)[0]
                    request.session['stid']=qry.sid
                    return render(request,'student.html')
                else:
                    return HttpResponse('login unsuccesful')    


def addfaculty(request):
    if request.method=='POST':
        names=request.POST.get('username')
        password=request.POST.get('password')
        b=faculty(username=names,password=password)
        b.save()
    return render(request,'addfact.html')


def factsign(request):
    if request.method=='POST':
        name=request.POST.get('name')
        factid=request.POST.get('factid')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        qualification=request.POST.get('qualification')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
    
        assbatch=request.POST.get('assbatch')
        c=facultysignup(name=name,factid=factid,address=address,dob=dob,gender=gender,qualification=qualification,mobile=mobile,email=email,assbatch=assbatch)
        c.save()
    return render(request,'faculty.html')


def signupstud(request):
    if request.method=='POST':
        sid=request.POST.get('sid')
        admno=request.POST.get('admno')
        admdate=request.POST.get('admdate')
        name=request.POST.get('name')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        mobile=request.POST.get('mobile')
        guardian=request.POST.get('guardian')
        batch=request.POST.get('batch')
        email=request.POST.get('email')
        password=request.POST.get('password')

        d=student(sid=sid,admno=admno,admdate=admdate,name=name,address=address,dob=dob,gender=gender,mobile=mobile,guardian=guardian,batch=batch,email=email,password=password)
        d.save()
    return render(request,'studentregistration.html')


def studattan(request):
    if request.method=='POST':
        sid=request.POST.get('sid')
        date=request.POST.get('date')
        name=request.POST.get('name')
        hours1status=request.POST.get('hours1status')
        hours2status=request.POST.get('hours2status')
        hours3status=request.POST.get('hours3status')
        hours4status=request.POST.get('hours4status')
        

        e=studentattantance(sid=sid,date=date,name=name,hours1status=hours1status,hours2status=hours2status,hours3status=hours3status,hours4status=hours4status)
        e.save()
    return render(request,'stdattantance.html')


def stdleave(request):
    if request.method=='POST':

        name=request.POST.get('name')
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        reason=request.POST.get('reason')
        f=sleave(name=name,fromdate=fromdate,todate=todate,reason=reason)
        f.save()
    return render(request,'studentleave.html')

def facleave(request):
    if request.method=='POST':

        name=request.POST.get('name')
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        reason=request.POST.get('reason')
        f=fleave(name=name,fromdate=fromdate,todate=todate,reason=reason)
        f.save()
    return render(request,'facultyleave.html')

def studmark(request):
    if request.method=='POST':
        sid=request.POST.get('sid')
        name=request.POST.get('name')
        assessmentno=request.POST.get('assessmentno')
        sub1mark=request.POST.get('sub1mark')
        sub2mark=request.POST.get('sub2mark')
        sub3mark=request.POST.get('sub3mark')
        percentage=request.POST.get('percentage')
        h=studentmark(sid=sid,name=name,assessmentno=assessmentno,sub1mark=sub1mark,sub2mark=sub2mark,sub3mark=sub3mark,percentage=percentage)
        h.save()
    return render(request,'studentmark.html') 


def detailsstudent(request):
    queryset=student.objects.all().filter(name=request.session['usernm'])
    return render(request,'personaldetails.html',{'authors':queryset})
def markview(request):
    querysett=studentmark.objects.all().filter(sid=request.session['stid'])
    return render(request,'viewmark.html',{'authorss':querysett})
def attantanceview(request):
    querysettt=studentattantance.objects.all().filter(sid=request.session['stid'])
    return render(request,'viewattantance.html',{'authorsss':querysettt})

def studview(request):
    querysettttt=student.objects.all().filter()
    return render(request,'viewstudt.html',{'authorsssss':querysettttt})

def facview(request):
    querysetttt=facultysignup.objects.all().filter()
    return render(request,'viewfac.html',{'authorssss':querysetttt})


