from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.models import *
# Create your views here.


def create_scl(request):
    ESFO=Schoolform()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=Schoolform(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['Sname']
            sp=SFDO.cleaned_data['Sprincipal']
            sl=SFDO.cleaned_data['Slocation']
            e=SFDO.cleaned_data['Email']
            re=SFDO.cleaned_data['Remail']
            SO=School.objects.get_or_create(Sname=sn,Sprincipal=sp,Slocation=sl,Email=e,Remail=re)[0]
            SO.save()
            return HttpResponse('school created')
        else:
            return HttpResponse('invalid data')
    



    return render(request,'create_scl.html',d)