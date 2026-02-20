from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1> welcome Django's world ! </h1>")
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
def gallary(request):
    return render(request,"gallary.html")
def faq(request):
    return render(request,"faq.html")

def add(request):
    if request.method=="POST":
        a=request.POST["Fno"]
        b=request.POST["Sno"]
        result=int(a)+int(b)
        return render(request,"add.html",context={"res":result})

    return render(request,"add.html")

def mul(request):
    if request.method=="POST":
        a=request.POST["Fno"] 
        b=request.POST["Sno"]
        result=int(a)*int(b)
        return render(request,"multiple.html", context={"multi":result})
    
    return render(request,"multiple.html")


def calculator(request):
        result=0
        if request.method == "POST":
            a =request.POST["Fno"]
            b =request.POST["Sno"]
            btn =request.POST["btn"]

            if btn =="ADD":
                result=int(a)+int(b)
            elif btn =="SUB":
                result=int(a)-int(b)
            elif btn =="MUL":
                result=int(a)*int(b)
            elif btn =="DIV":
                result=int(a)//int(b)
            return render(request,"calculator.html", context={"cal":result})
        return render(request,"calculator.html")
        
        


          
            
    
        


          
