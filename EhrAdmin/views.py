from django.shortcuts import render, redirect
from Register.models import Register_Master
from EhrAdmin.models import adminprofile_master
# Create your views here.

def adminviewprofile(request):
    email=request.session.get('email')
    ob=Register_Master.objects.get(Email=email)
    ob1=adminprofile_master.objects.get(email=ob)

    return render(request,'adminviewprofile.html',{'data':ob,'data1':ob1})

def adminprofile(request):
    email=request.session.get("email")
    ob=Register_Master.objects.get(Email=email)
    if request.method=="POST":
        image_file=request.FILES['image']
        print(image_file)
        doc_file= request.FILES['uploaded_doc']
        profile_update_obj,created=adminprofile_master.objects.get_or_create(email=ob)
        print(profile_update_obj)
    
        if image_file:
            profile_update_obj.Image=image_file
        if doc_file:
            profile_update_obj.Document=doc_file
        profile_update_obj.save()
        ob.Name=request.POST.get('name',ob.Name)
        ob.Email=request.POST.get('email',ob.Email)
        ob.Mobile=request.POST.get('mobile',ob.Mobile)
        ob.Password=request.POST.get('password',ob.Password)
        ob.Address=request.POST.get('ads',ob.Address)
        ob.DOB=request.POST.get('dob',ob.DOB)
        ob.Gender=request.POST.get('gender',ob.Gender)
        ob.save()
        return redirect('adminprofile')
    return render(request,"adminprofile.html",{"adata":ob})




def aviewdata(request):
    ob=Register_Master.objects.all()
    if request.method=="POST":
        email=request.POST['email']
        btn=request.POST['btn']
        if btn=="delete":
            Register_Master.objects.get(Email=email).delete()
            return redirect("aviewdata")
        if btn=="edit":
            data=Register_Master.objects.get(Email=email)
            return render(request,"edit.html",{'user':data})
    return render(request, "aviewdata.html",{'data':ob})

def update(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        gender=request.POST['gender']
        address=request.POST['address']
        status=request.POST['status']
        Register_Master.objects.filter(Email=email).update(Name=name,Mobile=mobile,Gender=gender,Address=address,Status=status)
        return redirect("aviewdata")
    return render(request,"edit.html")
        

def Ahome(request):
    username=request.session.get('name')
    return render(request,"Ahome.html",{'aname':username})