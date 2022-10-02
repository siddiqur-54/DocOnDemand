from django.contrib import admin
from django.urls import path, include
from appointment import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.patient_login, name="patient_login"),
    
    path('admin_home', views.admin_home, name="admin_home"),
    path('admin_login', views.admin_login, name="admin_login"),
    path('admin_pending_doctors', views.admin_pending_doctors, name="admin_pending_doctors"),
    path('admin_approve_doctor/<int:pid>', views.admin_approve_doctor, name="admin_approve_doctor"),
    path('admin_delete_patient/<int:pid>', views.admin_delete_patient, name="admin_delete_patient"),
    path('admin_view_patients', views.admin_view_patients, name="admin_view_patients"),
    path('admin_view_doctors', views.admin_view_doctors, name="admin_view_doctors"),
    path('admin_delete_pending_doctor/<int:pid>', views.admin_delete_pending_doctor, name="admin_delete_pending_doctor"),
    path('admin_delete_approved_doctor/<int:pid>', views.admin_delete_approved_doctor, name="admin_delete_approved_doctor"),
    path('admin_change_password', views.admin_change_password, name="admin_change_password"),
    path('admin_view_profile_patient/<int:pid>', views.admin_view_profile_patient, name="admin_view_profile_patient"),
    path('admin_view_profile_doctor/<int:pid>', views.admin_view_profile_doctor, name="admin_view_profile_doctor"),
    path('admin_patient_logout', views.admin_patient_logout, name="admin_patient_logout"),
    path('admin_reject_doctor/<int:pid>', views.admin_reject_doctor, name="admin_reject_doctor"),

    path('doctor_signup', views.doctor_signup, name="doctor_signup"),
    path('doctor_login', views.doctor_login, name="doctor_login"),
    path('doctor_home', views.doctor_home, name="doctor_home"),
    path('doctor_add_appointment', views.doctor_add_appointment, name="doctor_add_appointment"),
    path('doctor_appointments_list', views.doctor_appointments_list, name="doctor_appointments_list"),
    path('doctor_delete_own', views.doctor_delete_own, name="doctor_delete_own"),
    path('doctor_delete_appointment/<int:pid>', views.doctor_delete_appointment, name="doctor_delete_appointment"),
    path('doctor_edit_appointment/<int:pid>', views.doctor_edit_appointment, name="doctor_edit_appointment"),
    path('doctor_appointment_takers/<int:pid>', views.doctor_appointment_takers, name="doctor_appointment_takers"),
    path('doctor_view_profile_patient/<int:pid>', views.doctor_view_profile_patient, name="doctor_view_profile_patient"),
    path('doctor_appointment_profile/<int:pid>', views.doctor_appointment_profile, name="doctor_appointment_profile"),
    path('doctor_change_password', views.doctor_change_password, name="doctor_change_password"),
    path('doctor_logout', views.doctor_logout, name="doctor_logout"),
    path('doctor_edit_profile', views.doctor_edit_profile, name="doctor_edit_profile"),

    path('patient_login', views.patient_login, name="patient_login"),
    path('patient_signup', views.patient_signup, name="patient_signup"),
    path('patient_home', views.patient_home, name="patient_home"),
    path('patient_appointments_taken', views.patient_appointments_taken, name="patient_appointments_taken"),
    path('patient_latest_appointments', views.patient_latest_appointments, name="patient_latest_appointments"), 
    path('patient_take_appointment/<int:pid>', views.patient_take_appointment, name="patient_take_appointment"),
    path('patient_delete_own', views.patient_delete_own, name="patient_delete_own"),
    path('patient_undo_appointment/<int:pid>', views.patient_undo_appointment, name="patient_undo_appointment"),
    path('patient_change_password', views.patient_change_password, name="patient_change_password"),
    path('patient_edit_profile', views.patient_edit_profile, name="patient_edit_profile"),
    path('patient_appointment_profile_latest/<int:pid>', views.patient_appointment_profile_latest, name="patient_appointment_profile_latest"),
    path('patient_appointment_profile_taken/<int:pid>', views.patient_appointment_profile_taken, name="patient_appointment_profile_taken"),
]