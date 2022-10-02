from django.shortcuts import render,redirect
from appointment.models import Patient, Doctor, Appointment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date


# Create your views here.

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = request.user
    if not user.is_staff:
        return redirect('admin_login')
    error = ""
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']

        user.first_name = fname
        user.last_name = lname
        user.email = email

        try:
            user.save()
            error="no"
        except:
            error="yes"
    d = {'user': user, 'error': error}
    return render(request, 'admin_home.html', d)

def admin_change_password(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if not request.user.is_staff:
        return redirect('admin_login')
    error = ""
    if request.method=="POST":
        currentPass = request.POST['currentpassword']
        newPass = request.POST['newpassword']

        try:
            user = User.objects.get(id=request.user.id)
            if user.check_password(currentPass):
                user.set_password(newPass)
                user.save()
                error="no"
            else:
                error="yeah"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'admin_change_password.html', d)

def admin_view_profile_patient(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    patient = Patient.objects.get(id=pid)
    d = {'patient': patient}
    return render(request, 'admin_view_profile_patient.html', d)

def admin_patient_logout(request):
    if request.user.is_staff:
        logout(request)
        return redirect('admin_login')
    logout(request)
    return redirect('patient_login')


def admin_view_profile_doctor(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    doctor = Doctor.objects.get(id=pid)
    d = {'doctor': doctor}
    return render(request, 'admin_view_profile_doctor.html', d)

def admin_login(request):
    error=""
    if request.method=="POST":
        uname= request.POST['username']
        pword= request.POST['password']
        user= authenticate(username=uname, password=pword)
        try:
            if user.is_staff:
                login(request, user)
                error= "no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error': error}
    return render(request, 'admin_login.html',d)

def admin_approve_doctor(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    doctor = Doctor.objects.get(id=pid)
    doctor.status="Approved"
    doctor.save()
    return redirect('admin_pending_doctors')


def admin_reject_doctor(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    doctor = Doctor.objects.get(id=pid)
    doctor.status="Pending"
    doctor.save()
    return redirect('admin_view_doctors')


def admin_pending_doctors(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Doctor.objects.filter(status='Pending')
    d = {'data': data}
    return render(request, 'admin_pending_doctors.html',d)

def admin_view_patients(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if not request.user.is_staff:
        return redirect('admin_login')
    data = Patient.objects.all()
    d = {'data': data}
    return render(request, 'admin_view_patients.html',d)


def admin_view_doctors(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if not request.user.is_staff:
        return redirect('admin_login')
    data = Doctor.objects.filter(status="Approved")
    d = {'data': data}
    return render(request, 'admin_view_doctors.html',d)


def admin_delete_patient(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    patient = User.objects.get(id=pid)
    patient.delete()
    return redirect('admin_view_patients')

def admin_delete_pending_doctor(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    doctor = User.objects.get(id=pid)
    doctor.delete()
    return redirect('doctors_pending')


def admin_delete_approved_doctor(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    doctor = User.objects.get(id=pid)
    doctor.delete()
    return redirect('admin_view_doctors')


def doctor_view_profile_patient(request,pid):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    patient = Patient.objects.get(id=pid)
    d = {'patient': patient}
    return render(request, 'doctor_view_profile_patient.html', d)

def doctor_appointment_profile(request,pid):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    appointment = Appointment.objects.get(id=pid)
    d = {'appointment': appointment}
    return render(request, 'doctor_appointment_profile.html', d)

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
    return render(request, 'doctor_change_password.html', d)


def doctor_home(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    user = request.user
    doctor = Doctor.objects.get(user=user)
    d = {'doctor': doctor}
    return render(request, 'doctor_home.html', d)


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
    return render(request, 'doctor_edit_profile.html', d)



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
    return render(request, 'doctor_login.html',d)


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
    return render(request, 'doctor_signup.html', d)


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
    return render(request, 'doctor_add_appointment.html',d)


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
    return render(request, 'doctor_edit_appointment.html',d)

def doctor_appointment_takers(request,pid):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    appointment = Appointment.objects.get(id=pid)
    patient = appointment.patient.all()
    d = {'patient':patient}
    return render(request, 'doctor_appointment_takers.html', d)


def doctor_appointments_list(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    user = request.user
    doctor = Doctor.objects.get(user=user)
    appointment = Appointment.objects.filter(doctor=doctor)
    d = {'appointment':appointment}
    return render(request, 'doctor_appointments_list.html', d)


def patient_appointments_taken(request):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    user = request.user
    patient = Patient.objects.get(user=user)
    appointment = Appointment.objects.filter(patient=patient)
    d = {'appointment':appointment}
    return render(request, 'patient_appointments_taken.html', d)


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
    return render(request, 'patient_latest_appointments.html', d)


def patient_appointment_profile_latest(request,pid):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    appointment = Appointment.objects.get(id=pid)
    d = {'appointment': appointment}
    return render(request, 'patient_appointment_profile_latest.html', d)


def patient_appointment_profile_taken(request,pid):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    appointment = Appointment.objects.get(id=pid)
    d = {'appointment': appointment}
    return render(request, 'patient_appointment_profile_taken.html', d)


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
    return render(request, 'patient_change_password.html', d)



def patient_home(request):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    user = request.user
    patient= Patient.objects.get(user=user)
    d = {'patient': patient}
    return render(request, 'patient_home.html', d)

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
    return render(request, 'patient_edit_profile.html', d)

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
    return render(request, 'patient_login.html',d)

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
    return render(request, 'patient_signup.html',d)