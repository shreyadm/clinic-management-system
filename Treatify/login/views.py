from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home_page.html',{'name': 'Riyaa'})
    
def success(request):
    user = request.POST['usrname']
    password = request.POST['pass']

    return render(request,'login_success.html',{"user": user,"pas":password})    