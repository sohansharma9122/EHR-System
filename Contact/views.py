from django.shortcuts import render
from .models import Contact_Master

# Create your views here.
def Contact(request):
    if request.method=="POST":
        UserName=request.POST["name"]
        email=request.POST["email"]
        mobile=request.POST["mob"]
        feedback=request.POST["feedback"]

        ob=Contact_Master.objects.create(Name=UserName,Mobile=mobile,Email=email,Feedback=feedback)
        ob.save()
        return render(request,"Contact_Details.html",{"MSG": "Feedback submitted successful...."})


    return render(request,"Contact_Details.html")


