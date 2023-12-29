from django.urls import path
from appointment import views
from doctor import views

urlpatterns = [
    path('', views.doctor_login, name="doctor_login"),
    path('doctor_signup', views.doctor_signup, name="doctor_signup"),
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
    path('doctor_login', views.doctor_login, name="doctor_login"),
]