from django.shortcuts import render,redirect
from appointment.models import Patient, Doctor, Appointment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date


# Create your views here.
def doctor_view_profile_patient(request,pid):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    patient = Patient.objects.get(id=pid)
    d = {'patient': patient}
    return render(request, 'doctors/doctor_view_profile_patient.html', d)


def doctor_appointment_profile(request,pid):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    appointment = Appointment.objects.get(id=pid)
    d = {'appointment': appointment}
    return render(request, 'doctors/doctor_appointment_profile.html', d)


def doctor_change_password(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    error = ""
    if request.method=="POST":
        currentPass = request.POST['currentpassword']
        newPass = request.POST['newpassword']
        try:
            doctor = User.objects.get(id=request.user.id)
            if doctor.check_password(currentPass):
                doctor.set_password(newPass)
                doctor.save()
                error="no"
            else:
                error="yeah"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'doctors/doctor_change_password.html', d)


def doctor_home(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    user = request.user
    doctor = Doctor.objects.get(user=user)
    d = {'doctor': doctor}
    return render(request, 'doctors/doctor_home.html', d)


def doctor_edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    user = request.user
    doctor = Doctor.objects.get(user=user)
    error = ""
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        contact = request.POST['contact']
        gender = request.POST['gender']
        medical = request.POST['medical']
        position = request.POST['position']
        specialities = request.POST['specialities']
        doctor.user.first_name = fname
        doctor.user.last_name = lname
        doctor.contact = contact
        doctor.gender = gender
        doctor.medical = medical
        doctor.position = position
        doctor.specialities = specialities
        try:
            doctor.save()
            doctor.user.save()
            error="no"
        except:
            error="yes"
    d = {'doctor': doctor, 'error': error}
    return render(request, 'doctors/doctor_edit_profile.html', d)


def doctor_login(request):
    error=""
    if request.method=="POST":
        uname= request.POST['username']
        pword= request.POST['password']
        user= authenticate(username=uname, password=pword)
        if user:
            try:
                doctor = Doctor.objects.get(user=user)
                if doctor.type == "doctor" and doctor.status=="Approved":
                    login(request,user)
                    error="no"
                else:
                    error="not"
            except:
                error="yes"
        else:
            error="yes"
    d= {'error' : error}
    return render(request, 'doctors/doctor_login.html',d)


def doctor_logout(request):
    logout(request)
    return redirect('doctor_login')


def doctor_signup(request):
    error = ""
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['email']
        password = request.POST['password']
        image = request.FILES['image']
        contact = request.POST['contact']
        gender = request.POST['gender']
        medical = request.POST['medical']
        position = request.POST['position']
        specialities = request.POST['specialities']  
        try:
            doctor= User.objects.create_user(username=username,email=email,password=password)
            doctor.first_name=fname
            doctor.last_name=lname
            doctor.save()
            Doctor.objects.create(image=image, contact=contact, gender=gender, medical=medical, position=position, specialities=specialities, type="doctor", status="Pending", user=doctor)
            error="no"
        except:
            error="yes"
    d={'error': error}
    return render(request, 'doctors/doctor_signup.html', d)


def doctor_delete_own(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    doctor = request.user
    doctor.delete()
    return redirect('doctor_login')
    

def doctor_delete_appointment(request,pid):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    appointment = Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('doctor_appointments_list')


def doctor_add_appointment(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    error = ""
    if request.method=="POST":
        title = request.POST['title']
        description = request.POST['description']
        adate = request.POST['adate']
        atime = request.POST['atime']
        deadline = request.POST['deadline']
        fee = request.POST['fee']
        location = request.POST['location']

        user = request.user
        doctor = Doctor.objects.get(user=user)
        
        try:
            Appointment.objects.create(title=title, description=description, post_date=date.today(), date=adate, time=atime, deadline=deadline, fee=fee, location=location, doctor=doctor)
            error="no"
        except:
            error="yes"
    d={'error': error}
    return render(request, 'doctors/doctor_add_appointment.html',d)


def doctor_edit_appointment(request,pid):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    error = ""
    appointment = Appointment.objects.get(id=pid)
    if request.method=="POST":
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        time = request.POST['time']
        deadline = request.POST['deadline']
        fee = request.POST['fee']
        location = request.POST['location']
        appointment.title = title
        appointment.description = description
        appointment.time = time
        appointment.fee = fee
        appointment.location = location
        if date:
            appointment.date=date
        if deadline:
            appointment.deadline=deadline
        try:
            appointment.save()
            error="no"
        except:
            error="yes"
    d={'error': error, 'appointment':appointment}
    return render(request, 'doctors/doctor_edit_appointment.html',d)


def doctor_appointment_takers(request,pid):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    appointment = Appointment.objects.get(id=pid)
    patient = appointment.patient.all()
    d = {'patient':patient}
    return render(request, 'doctors/doctor_appointment_takers.html', d)


def doctor_appointments_list(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    user = request.user
    doctor = Doctor.objects.get(user=user)
    appointment = Appointment.objects.filter(doctor=doctor)
    d = {'appointment':appointment}
    return render(request, 'doctors/doctor_appointments_list.html', d)