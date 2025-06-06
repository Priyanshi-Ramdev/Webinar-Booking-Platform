from django.urls import path, include
from . import views
from .views import user_dashboard
from .views import webinar_detail, booking_confirmation, booking_confirmation_existing, cancel_booking

urlpatterns = [
     path('', views.homepage, name='homepage'),
    path('signup/', views.signup_view, name='signup'),  
    path('accounts/login/', views.login_view, name='login'),
     path('logout/', views.logout_view, name='logout'),
    path('dashboard/', user_dashboard, name='dashboard'),
   
    path('webinars/<int:webinar_id>/', webinar_detail, name='webinar_detail'),
    path('booking-confirmation/<int:booking_id>/', booking_confirmation, name='booking_confirmation'),
    path('already-booked/<int:webinar_id>/', booking_confirmation_existing, name='booking_confirmation_existing'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('webinars/', views.webinar_list, name='webinar_list'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),


    path('accounts/profile/', views.profile, name='profile'),
    path('webinars/', views.webinar_list, name='webinar_list'),
    path('webinars/<int:webinar_id>/', views.webinar_detail, name='webinar_detail'),
    path('booking_confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
   

]

