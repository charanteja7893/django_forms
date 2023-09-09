from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
def student(request):
    SFO=student_forms()
    d={'SFO':SFO}
    if request.method =='POST':
        SFDO=student_forms(request.POST)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('invalid')

    return render(request,'student.html',d)