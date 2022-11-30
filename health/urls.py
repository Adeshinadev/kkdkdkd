# Class which handles all path patterns, I.e. a user clicks a link and navigates to a new page.
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

# path patterns, I.e. all url's for the application.
urlpatterns = [
               # Pattern for the login page.
               path('login/', views.login_view, name='login'),
               # Pattern which will be used if the user wishes to logout.
               path('logout/', views.logout_view, name='logout'),
               # Pattern for displaying the users schedule.
               path('schedule/', views.schedule, name='schedule'),
               # Pattern for displaying the users current prescriptions.
               path('prescriptions/', views.prescriptions, name='prescriptions'),
               # Pattern for displaying the users current messages, I.e. send a new message.
               path('messages/', views.messages, name='messages'),
               # Pattern for displaying the users current conversations, I.e. past messages.
               path('conversation/<id>', views.conversation, name='conversation'),
               # Pattern for removing a prescription, requires specific account.
               path('delete_prescription/<prescription_id>', views.delete_prescription, name='delete_prescription'),
               # Pattern for editing a prescription, requires specific account.
               path('edit_prescription/<prescription_id>', views.prescription_form, name='edit_prescription'),
               # Pattern for adding a prescription, requires specific account.
               path('add_prescription/', views.add_prescription_form, name='add_prescription'),
               # Pattern for removing a appointment, requires specific account.
               path('delete_appointment/<appointment_id>', views.delete_appointment, name='delete_appointment'),
               # Pattern for editing an appointment, requires specific account.
               path('edit_appointment/<appointment_id>', views.appointment_form, name='edit_appointment'),
               # Pattern for adding an appointment, requires specific account.
               path('add_appointment/', views.add_appointment_form, name='add_appointment'),
               # Pattern for adding a group, I.e. messaging, requires specific account.
               path('add_group/', views.add_group, name='add_group'),
               # Pattern for displaying a user medical informaiton, I.e. a patients information, requires specific
               # account.
               path('medical_information/<user_id>', views.medical_information, name='medical_information'),
               # Pattern for displaying a users information, I.e. a users profile.
               path('users/me/', views.my_medical_information, name='my_medical_information'),
               # Pattern for creating a new account.
               path('signup/', views.signup, name='signup'),
               # Pattern for exporting a users information, downloads a users information.
               path('export/<id>', views.export, name='export'),
               # Pattern for exporting a users information, downloads a users information.
               # path('users/me/info.json/?$', views.export_me, name='export_me'),
               # Pattern for detecting a user.
               path('users/?$', views.users, name='users'),
               # Pattern for displaying all logs for the application, I.e. has something changed,
               # and what, and who, requires specific account.
               path('logs/', views.logs, name='logs'),
               # Pattern for displaying the page media_gallery.html, I.e. a users documents.
               path('media_gallery/<user_id>', views.media_gallery, name='media_gallery'),
               # Pattern for navigating to the home page.
               path('', views.home, name='home'),
               path('home', views.home, name='home'),
               ]
