from django.shortcuts import render,redirect
from appointment.models import Patient, Doctor, Appointment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date


# Create your views here.
def patient_appointments_taken(request):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    user = request.user
    patient = Patient.objects.get(user=user)
    appointment = Appointment.objects.filter(patient=patient)
    d = {'appointment':appointment}
    return render(request, 'patients/patient_appointments_taken.html', d)


def patient_take_appointment(request,pid):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    user = request.user
    patient = Patient.objects.get(user=user)
    appointment = Appointment.objects.get(id=pid)
    appointment.patient.add(patient)
    return redirect('patient_appointments_taken')


def patient_undo_appointment(request,pid):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    user = request.user
    patient = Patient.objects.get(user=user)
    appointment = Appointment.objects.get(id=pid)
    appointment.patient.remove(patient)
    return redirect('patient_latest_appointments')


def patient_latest_appointments(request):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    user = request.user
    patient = Patient.objects.get(user= user)
    appointment= Appointment.objects.exclude(patient=patient)
    d = {'appointment':appointment}
    return render(request, 'patients/patient_latest_appointments.html', d)


def patient_appointment_profile_latest(request,pid):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    appointment = Appointment.objects.get(id=pid)
    d = {'appointment': appointment}
    return render(request, 'patients/patient_appointment_profile_latest.html', d)


def patient_appointment_profile_taken(request,pid):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    appointment = Appointment.objects.get(id=pid)
    d = {'appointment': appointment}
    return render(request, 'patients/patient_appointment_profile_taken.html', d)


def patient_change_password(request):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    error = ""
    if request.method=="POST":
        currentPass = request.POST['currentpassword']
        newPass = request.POST['newpassword']
        try:
            patient = User.objects.get(id=request.user.id)
            if patient.check_password(currentPass):
                patient.set_password(newPass)
                patient.save()
                error="no"
            else:
                error="yeah"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'patients/patient_change_password.html', d)


def patient_home(request):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    user = request.user
    patient= Patient.objects.get(user=user)
    d = {'patient': patient}
    return render(request, 'patients/patient_home.html', d)


def patient_edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    user = request.user
    patient= Patient.objects.get(user=user)
    error = ""
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        contact = request.POST['contact']
        height = request.POST['height']
        weight = request.POST['weight']
        gender = request.POST['gender']
        marital_status = request.POST['marital_status']
        blood_group = request.POST['blood_group']
        birth_date = request.POST['birth_date']
        patient.user.first_name = fname
        patient.user.last_name = lname
        patient.contact = contact
        patient.height = height
        patient.weight = weight
        patient.gender = gender
        patient.marital_status = marital_status
        patient.blood_group = blood_group
        if birth_date:
            patient.birth_date=birth_date
        try:
            patient.save()
            patient.user.save()
            error="no"
        except:
            error="yes"
    d = {'patient': patient, 'error': error}
    return render(request, 'patients/patient_edit_profile.html', d)


def patient_login(request):
    error=""
    if request.method=="POST":
        uname= request.POST['username']
        pword= request.POST['password']
        user= authenticate(username=uname, password=pword)
        if user:
            try:
                patient = Patient.objects.get(user=user)
                if patient.type == "patient":
                    login(request,user)
                    error="no"
                else:
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"
    d= {'error' : error}
    return render(request, 'patients/patient_login.html',d)


def patient_delete_own(request):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    patient = request.user
    patient.delete()
    return redirect('patient_login')


def patient_signup(request):
    error = ""
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['email']
        password = request.POST['password']
        image = request.FILES['image']
        contact = request.POST['contact']
        height = request.POST['height']
        weight = request.POST['weight']
        gender = request.POST['gender']
        marital_status = request.POST['marital_status']
        blood_group = request.POST['blood_group']
        birth_date = request.POST['birth_date']
        try:
            patient= User.objects.create_user(username=username,email=email,password=password)
            patient.first_name=fname
            patient.last_name=lname
            patient.save()
            Patient.objects.create(contact=contact, image=image, height=height, weight=weight, gender=gender, marital_status=marital_status, blood_group=blood_group, birth_date=birth_date, type="patient", user=patient)
            error="no"
        except:
            error="yes"
    d={'error': error}
    return render(request, 'patients/patient_signup.html',d)