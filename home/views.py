from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
#added
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

#-------------------------------------------------------
#added

    #return HttpResponse("this is contact page")
    # 1. The Home Page (Protected)
def index(request):
    if request.user.is_anonymous:
        return redirect("/login/")
   
    return render(request,'index.html')

# 2. The Login Logic
def loginUser(request):
    if request.method == "POST":
        # Get data from the form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # FIX A: Remove quotes around username and password
        # FIX B: Pass 'request' as the first argument (good practice)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # FIX C: Actually log the user in to create the session
            login(request,user)
            return redirect("/") # Redirect to the index page
        else:
            # If password is wrong, reload login page with an error context
         return render(request,'login.html',{'error':'Invalid credentials'})
    # If it's a GET request (just visiting the page), show the form
    return render(request, 'login.html')

# 3. Logout
def logoutUser(request):
    logout(request)
    return redirect("/login/")


#--------------------------------------------------------
# Create your views here.

   # return HttpResponse("Welcome to index PAGE prathamesh kale patil")

def about(request):
        return render(request,'about.html')

    #return HttpResponse("this is about page")

def services(request):
         return render(request,'services.html')

    #return HttpResponse("this is services page")

def contact(request):
        if request.method =="POST":
               name = request.POST.get('name')
               email = request.POST.get('email')
               phone = request.POST.get('phone')
               desc = request.POST.get('desc')
               Contact.objects.create(name=name, 
                                      email=email, 
                                      phone=phone, 
                                      desc=desc, 
                                      date=datetime.today())
               messages.success(request, "Your Suggetions are Submitted Successfully!")
        return render(request,'contact.html')

