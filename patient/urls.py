
from django.urls import path
from appointment import views
from patient import views


urlpatterns = [
    path('', views.patient_login, name="patient_login"),
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
    path('patient_login', views.patient_login, name="patient_login"),
]