from django.shortcuts import render, HttpResponse
from app.forms import *
# Create your views here.

def register(request):
    UO = UserForm()
    d = {'UO':UO}
    if request.method == 'POST':
        UFDO = UserForm(request.POST)
        MUFDO = UFDO.save(commit=False)
        pw = UFDO.cleaned_data['password']
        MUFDO.set_password(pw)
        MUFDO.save()
        return HttpResponse('User Registered Successfully')
    return render(request, 'register.html', d)