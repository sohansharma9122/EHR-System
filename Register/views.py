from django.shortcuts import render
from .models import Register_Master

# Create your views here.
def Signup(request):
    if request.method=="POST":
        username=request.POST["name"]
        mobile=request.POST["mobile"]
        email=request.POST["email"]
        pwd=request.POST["pwd"]
        dob=request.POST["dob"]
        gender=request.POST["gender"]
        Address=request.POST["addr"]
        role=request.POST["role"]
    
        ob=Register_Master.objects.create(Name=username,Mobile=mobile,Email=email,Password=pwd,DOB=dob,Gender=gender,Address=Address,Role_Name=role)
        ob.save()
        return render(request,"signup.html",{"MSG": "Register successful...."})


    return render(request,"signup.html")