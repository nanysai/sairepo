from django.shortcuts import render
from testapp.models import School,College,Degree
# Create your views here.
def info(request):
    return render(request,'testapp/info.html')

def school(request):
    obj=School.objects.all().order_by('sno','sname')
    dict={'obj':obj}
    return render(request,'testapp/school.html',dict)

def college(request):
    obj=College.objects.all()
    dict={'obj':obj}
    return render(request,'testapp/college.html',dict)

def degree(request):
    obj=Degree.objects.all()
    dict={'obj':obj}
    return render(request,'testapp/degree.html',dict)