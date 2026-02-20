from django.shortcuts import render,redirect
from Register.models import Register_Master

# Create your views here.
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pwd']
        try:
            ob=Register_Master.objects.get(Email=email,Password=password)
            request.session['Name']=ob.Name
            request.session['email']=ob.Email
            # print(ob.Status)

            if ob.Status=='1':
                if ob.Role_Name=="Doctor":
                    return redirect ("Dhome")
                elif ob.Role_Name=="Staff":
                    return redirect ("Shome")
                elif ob.Role_Name=="Patient":
                    return redirect ("Phome")
                elif ob.Role_Name=="EhrAdmin":
                    return redirect ("Ahome")
            else:
                return render(request,'login.html',{'msg':"Waiting for admin Conformation !!!!!!"})
               
        except Exception as e:
            return render(request,"login.html",{"msg" : "invalid" + str(e)})
    return render(request,"login.html")