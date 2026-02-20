from django.shortcuts import render
from Register.models import Register_Master
from .forms import testForm

# Create your views here.

def add_test(request):
    formobj=testForm()
    if request.method=="POST":
        formobj=testForm(request.POST)
        if formobj.is_valid():
            formobj.save()
    return render(request,'Add_test.html',{'form':formobj})



# for Doctor and patient  view data 
def pd_viewdata(request):
    ob=Register_Master.objects.filter(Role_Name='Doctor')
    ob1=Register_Master.objects.filter(Role_Name='Patient')
    return render(request,"Patient_Doctor_data.html",{'data':ob,'data1':ob1})



def Shome(request):
    username=request.session.get('name')
    return render (request,"Shome.html",{'Sname':username})

