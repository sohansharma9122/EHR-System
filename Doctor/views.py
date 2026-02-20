from django.shortcuts import render,redirect,get_object_or_404
from Register.models import Register_Master
from Patient.models import Doctor_Appointment
from django.contrib import messages
from Doctor.models import *

# Create your views here.(request):  

def Doctorprofile(request):
    # Always use one session key (use lowercase for safety)
    user_email = request.session.get("email")

    if not user_email:
        messages.error(request, "Please login first!")
        return redirect("login")

    # This returns a SINGLE object (correct)
    ddata = Register_Master.objects.filter(Email=user_email).first()

    if not ddata:
        messages.error(request, "User not found in Register_Master!")
        return redirect("login")

    # Check if doctor profile exists
    profile = doctorprofile_master.objects.filter(email=ddata).first()

    if request.method == "POST":
        designation = request.POST.get("designation")
        image = request.FILES.get("image")
        document = request.FILES.get("uploaded_doc")

        # UPDATE PROFILE
        if profile:
            profile.Designation = designation

            if image:
                profile.Image = image

            if document:
                profile.Document = document

            profile.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("Doctorprofile")

        # CREATE NEW PROFILE
        else:
            profile = doctorprofile_master(
                email=ddata,
                Designation=designation,
                Image=image,
                Document=document
            )
            profile.save()

            messages.success(request, "Profile created successfully!")
            return redirect("Doctorprofile")

    return render(request, "doctorprofile.html", {"ddata": ddata, "profile": profile})



def viewdetails(request):
    if request.method=="POST":
        pid=request.POST["pid"]
        btn=request.POST["btn"]

        if btn == "ViewDetails":
            ob= Doctor_Appointment.objects.get(id=pid)
            return render(request,"patient_details.html",{"pdata":ob})
        elif btn=="submit":
            prescription_text = request.POST["prescription"]
            app = Doctor_Appointment.objects.get(id=pid)

            Prescription.objects.create(
                app_id=app,
                prescription_text=prescription_text
            )

            return redirect("display_appointment")
        return redirect("display_appointment")

    



def Pviewdata(request):
    ob=Register_Master.objects.filter(Role_Name='Patient')
    return render(request,"Patient_data.html",{'data':ob})

def display_appointment(request):
    email=request.session.get("email")
    ob1=Register_Master.objects.get(Email=email)
    ob=Doctor_Appointment.objects.filter(doct_email=ob1)
    return render(request,"display_appointment.html",{"appointments":ob})


def approve_appointment(request):
    if request.method == "POST":
        appointment_id = request.POST.get("appointment_id")
        appointment = get_object_or_404(Doctor_Appointment, id=appointment_id)
        appointment.status = "Approved"
        appointment.save()
        messages.success(request, f"Appointment for {appointment.p_name} has been approved.")
        return redirect("display_appointment")


def cancel_appointment(request):
    if request.method == "POST":
        appointment_id = request.POST.get("appointment_id")
        appointment = get_object_or_404(Doctor_Appointment, id=appointment_id)
        appointment.status = "Cancelled"
        appointment.save()
        messages.error(request, f"Appointment for {appointment.p_name} has been cancelled.")
        return redirect("display_appointment")


def Dhome(request):
    return render(request,'Dhome.html')