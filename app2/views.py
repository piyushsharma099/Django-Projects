from django.shortcuts import render,redirect,HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from app1.models import student
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request,'index.html')

def display(request):
    disp=student.objects.all()
    context={
        'disp': disp
    }
    return render(request,'display.html',context)

def add(request):
    if request.method=='POST':
        a=request.POST['title']
        b=request.POST['co_name']
        c=request.POST['abstract']
        d=request.POST['branch']
        e=request.POST['session']
        f=request.POST['team_m']
        new_stu=student(title=a,co_name=b,abstract=c,branch=d,session=e,team_m=f)
        new_stu.save()
        return HttpResponse("Student added Successfully ! ")
    elif request.method=='GET':
        return render(request,'add.html')
    else:
        return HttpResponse("An Error Occurred ! Student Has Not Been Added")

def remove(request,i_id=0):
    if i_id:
        try:
            stu_to_be_removed= student.objects.get(id=i_id)
            stu_to_be_removed.delete()
            return HttpResponse("Project removed successfully")
        except:
            return HttpResponse("Please Enter a Valid ID")
    rem=student.objects.all()
    context={
        'rem': rem
    }
    return render(request,'remove.html',context)

    #return render(request,'remove.html')

def filter(request):
    if request.method == 'POST':
        name=request.POST['name']
        branch=request.POST['branch']
        session=request.POST['session']
        stu=student.objects.all()
        if name:
            stu= stu.filter(Q(team_m__icontains=name))
        if branch:
            stu= stu.filter(branch__icontains=branch)
        if session:
            stu=stu.filter(session__icontains=session)
        context={
            'stu':stu
        }
        return render(request,'display.html',context)

    elif request.method=='GET':
        return render(request,'filter.html')
    
    else:
        return HttpResponse("NOT FOUND !")
    

def home(request):
    disp=student.objects.all()
    context={
        'disp': disp
    }
    return render(request,'home.html',context)

    #return render(request,"home.html")

def login(request):
    if request.method == 'POST':
        username=request.POST.get['username']
        password=request.POST.get['password']
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Successfully logged in")
            #return render(request,"app2/index.html",{})
            return redirect('index')
        else:
            messages.info(request,"Invalid credentials")
            #return render(request,"app2/login.html",{})
            return redirect('login')
    else:
        return render(request,'login.html')
    #return HttpResponse('login')

def logout(request):
    auth.logout(request)
    return redirect('home')


# def display(request):
#     disp=student.objects.all()
#     context={
#         'disp': disp
#     }
#     return render(request,'home.html',context)
