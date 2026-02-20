from django.shortcuts import render,redirect
from Register.models import Register_Master
from Patient .models import patientprofile_master
from Staff.models import Laboratory_test
from .models import *
# Create your views here.

def applytest(request):
    ob=PatientTestReport.objects.all()
    return render(request,"applytest.html",{"rdata":ob})

def viewlabtest(request):
    email = request.session.get("email")
    logged_in_user = Register_Master.objects.get(Email=email)
    if request.method == "POST":
        selected_ids = request.POST.getlist("selected_tests")
        patient = logged_in_user
        tests = Laboratory_test.objects.filter(test_id__in=selected_ids)
        total_price = sum(test.test_Price for test in tests)
        report = PatientTestReport.objects.create(patient=patient,total_price=total_price)
        report.tests.set(tests)
        report.save()
        request.session["last_report_id"] = report.report_id
        return redirect("testreport")
    ob = Laboratory_test.objects.all()
    return render(request, "viewlabtest.html", {"testdata": ob, "user": logged_in_user})


import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .models import PatientTestReport

def testreport(request):
    report_id = request.session.get("last_report_id")
    if not report_id:
        return redirect("viewlabtest")

    try:
        report = PatientTestReport.objects.get(pk=report_id)
    except PatientTestReport.DoesNotExist:
        return redirect("viewlabtest")

    # Initialize Razorpay client
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    # Create order only if payment not done yet
    order = None
    if not report.is_paid:
        order_amount = int(report.total_price * 100)  # ₹ to paise
        order_currency = "INR"
        order = client.order.create(dict(amount=order_amount, currency=order_currency, payment_capture="1"))
        report.razorpay_order_id = order["id"]
        report.save()

    return render(request, "testreport.html", {
        "report": report,
        "tests": report.tests.all(),
        "total_price": report.total_price,
        "order": order,
        "razorpay_key_id": settings.RAZORPAY_KEY_ID,
    })



@csrf_exempt
def payment_success(request):
    user_email = request.session.get("email")

    report = PatientTestReport.objects.filter(patient__Email=user_email).last()

    if report:
        report.is_paid = True
        report.razorpay_order_id = request.POST.get("razorpay_order_id")
        report.razorpay_payment_id = request.POST.get("razorpay_payment_id")
        report.save()

        # Session me reg_id bhi store kro (best practice)
        request.session["reg_id"] = report.patient.reg_id

        return render(request, "payment_success.html", {"report": report})

    return redirect("viewlabtest")


from django.template.loader import render_to_string

from django.http import HttpResponse
from xhtml2pdf import pisa


def download_report_pdf(request, report_id):
    user_email = request.session.get("email")

    report = PatientTestReport.objects.filter(
        report_id=report_id,
        patient__Email=user_email
    ).first()

    if not report:
        return HttpResponse("❌ Unauthorized Access")

    if not report.is_paid:
        return HttpResponse("⚠ Payment Pending")

    # ✅ PDF Logic
    template_path = "report_pdf.html"
    html = render_to_string(template_path, {"report": report})

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"attachment; filename=Lab_Report_{report_id}.pdf"

    pisa.CreatePDF(html, dest=response)
    return response






from .models import Doctor_Appointment
from .models import Doctor_Appointment

def patient_dashboard(request):
    Appointment = None  # Start with None to indicate no search yet
    searched = False

    if request.method == "POST":
        searched = True
        pmobile = request.POST['pmobile']
        if pmobile:
            Appointment = Doctor_Appointment.objects.filter(p_mobile=pmobile)

    return render(request, "patient_dashboard.html", {
        "msg": Appointment,
        "searched": searched
    })





def take_appointment(request):
    if request.method=="POST":
        doct_name=request.POST['dname']
        doct_email=request.POST['demail']
        demail=Register_Master.objects.get(Email=doct_email)
        doct_mobile=request.POST['dmobile']
        p_name=request.POST['pname']
        p_email=request.POST['pemail']
        p_mobile=request.POST['pmobile']
        p_dob=request.POST['pdob']
        p_address=request.POST['paddress']
        p_gender=request.POST['pgender']
        diseases=request.POST['diseases']

        ob=Doctor_Appointment.objects.create(
            doct_name=doct_name,
            doct_email=demail,
            doct_contact=doct_mobile,
            p_name=p_name,
            p_mobile=p_mobile,
            p_address=p_address,
            p_gender=p_gender,
            dob=p_dob,
            p_disease=diseases,

        )
        ob.save()
        return redirect("success")
 
    return render(request,"book_appointment.html")

def success(request):
    return render(request,"success_page.html")




## for staff view data
def pdviewdata(request):
    ob=Register_Master.objects.filter(Role_Name__iexact="Doctor")
    if request.method=="POST":
        demail=request.POST["email"]
        btn=request.POST["btn"]
        if btn=="Appointment":
            obj=Register_Master.objects.get(Email=demail)
            pemail=request.session.get('email')
            obj1=Register_Master.objects.get(Email=pemail)
            return render(request,"book_appointment.html",{"ddata":obj,'pdata':obj1})


    return render(request,'Pdviewdata.html',{'data':ob})

def patientprofile(request):
    email=request.session.get('email')
    ob=Register_Master.objects.get(Email=email)

    if request.method=="POST":
        image_file=request.FILES['image']
        doc_file=request.FILES['uploaded_doc']
        diseases=request.POST['disease']
        profile_update_obj,created=patientprofile_master.objects.get_or_create(email=ob)

        if image_file:
            profile_update_obj.Image=image_file
        if doc_file:
            profile_update_obj.Document=doc_file
        if diseases:
            profile_update_obj.Diseases=diseases
        profile_update_obj.save()
        ob.Name=request.POST.get('name',ob.Name)
        ob.Email=request.POST.get('email',ob.Email)
        ob.Mobile=request.POST.get('mobile',ob.Mobile)
        ob.Password=request.POST.get('pwd',ob.Password)
        ob.Address=request.POST.get('ads',ob.Address)
        ob.DOB=request.POST.get('dob',ob.DOB)
        ob.Gender=request.POST.get('gender',ob.Gender)
        ob.save()
        return redirect('patientprofile')
    return render(request,"patientprofile.html",{'pdata':ob})

def patientviewprofile(request):
    email=request.session.get('email')
    ob=Register_Master.objects.get(Email=email)
    return render(request,"patientviewprofile.html",{'data':ob})





def Phome(request):
    userName=request.session.get('Name')
    return render(request,"Phome.html",{'Pname':userName})




