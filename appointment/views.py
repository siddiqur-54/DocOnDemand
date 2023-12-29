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
    return render(request, 'admins/admin_home.html', d)


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
    return render(request, 'admins/admin_change_password.html', d)


def admin_view_profile_patient(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    patient = Patient.objects.get(id=pid)
    d = {'patient': patient}
    return render(request, 'admins/admin_view_profile_patient.html', d)


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
    return render(request, 'admins/admin_view_profile_doctor.html', d)


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
    return render(request, 'admins/admin_login.html',d)


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
    return render(request, 'admins/admin_pending_doctors.html',d)


def admin_view_patients(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if not request.user.is_staff:
        return redirect('admin_login')
    data = Patient.objects.all()
    d = {'data': data}
    return render(request, 'admins/admin_view_patients.html',d)


def admin_view_doctors(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if not request.user.is_staff:
        return redirect('admin_login')
    data = Doctor.objects.filter(status="Approved")
    d = {'data': data}
    return render(request, 'admins/admin_view_doctors.html',d)


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