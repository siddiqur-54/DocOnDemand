from django.urls import path
from appointment import views

urlpatterns = [
    path('', views.admin_login, name="admin_login"),
    path('admin_home', views.admin_home, name="admin_home"),
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
    path('admin_login', views.admin_login, name="admin_login"),
]