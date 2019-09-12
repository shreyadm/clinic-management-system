from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def login(request):
    if request.method == 'POST':
        usr = request.POST['usrname']
        pass1 = request.POST['pass']
        user = auth.authenticate(username=usr,password=pass1)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print("Invalid credentials")    
    else:
          return render(request,'login_page.html')  
def register(request):
    if request.method == 'POST':
        usr = request.POST['usrname']
        pass1 = request.POST['pass']
        pass2 = request.POST['cpass']
        mailID = request.POST['mailId']

        if pass1==pass2:
            if User.objects.filter(username=usr).exists():
                print("Username taken")
            elif User.objects.filter(email=mailID).exists():
                print("Email taken")
            else:
                user = User.objects.create_user(username=usr,password=pass1,email=mailID)
                user.save()
                print("User created!")
                return redirect('/')
        else:
            print("Password not matching!")
    else:    
        return render(request,'register_page.html')