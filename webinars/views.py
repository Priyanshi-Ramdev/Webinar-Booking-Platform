from django.db import IntegrityError
from django.shortcuts import render,redirect, get_object_or_404
from .models import Webinar, Booking
from .forms import BookingForm
from django.core.mail import send_mail
from django.conf import settings
from .forms import EditProfileForm
from datetime import date
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Login ke baad dashboard pe redirect
        else:
            context = {'error': 'Invalid username or password'}
            return render(request, 'webinars/login.html', context)

    return render(request, 'webinars/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Add validation & error handling as needed

        if User.objects.filter(username=username).exists():
            context = {'error': 'Username already exists'}
            return render(request, 'webinars/signup.html', context)

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('dashboard')

    return render(request, 'webinars/signup.html')



def logout_view(request):
    logout(request)
    return redirect('login')  # Logout ke baad login page pe bhejein

def webinar_list(request):
    webinars = Webinar.objects.all()
    return render(request, 'webinars/webinar_list.html', {'webinars': webinars})

def homepage(request):
    webinars = Webinar.objects.all().order_by('date')[:3]  # fetch top 3
    return render(request, 'webinars/home.html', {'webinars': webinars})


def send_booking_confirmation_email(booking):
    subject = f"Booking Confirmation: {booking.webinar.title}"
    message = f"Hello {booking.user.username},\n\nYou have successfully booked a spot for the webinar {booking.webinar.title} on {booking.webinar.date}.\n\nThank you for your booking!"
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,  # From address
        [booking.user.email]  # To address
    )

@login_required
def webinar_detail(request, webinar_id):
    webinar = get_object_or_404(Webinar, id=webinar_id)

    # GET request (show booking form or message if already booked)
    if request.method == "GET":
        if Booking.objects.filter(user=request.user, webinar=webinar, status='booked').exists():
            messages.info(request, "You have already booked this webinar.")
            return redirect("booking_confirmation_existing", webinar_id=webinar.id)

        form = BookingForm()
        return render(request, 'webinars/webinar_detail.html', {'webinar': webinar, 'form': form})

    # POST request (create booking safely)
    elif request.method == "POST":
        if Booking.objects.filter(user=request.user, webinar=webinar, status='booked').exists():
            messages.info(request, "You already booked this webinar.")
            return redirect("booking_confirmation_existing", webinar_id=webinar.id)

        try:
            # Optional: clean up old cancelled booking
            Booking.objects.filter(user=request.user, webinar=webinar, status='cancelled').delete()

            booking = Booking.objects.create(
                user=request.user,
                webinar=webinar,
                status='booked'
            )
            send_booking_confirmation_email(booking)  # optional
            return redirect("booking_confirmation", booking_id=booking.id)

        except IntegrityError:
            messages.warning(request, "You already booked this webinar.")
            return redirect("booking_confirmation_existing", webinar_id=webinar.id)

    # If neither GET nor POST
    form = BookingForm()
    return render(request, 'webinars/webinar_detail.html', {'webinar': webinar, 'form': form})

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'webinars/booking_confirmation.html', {'booking': booking})

def send_booking_confirmation_email(booking):
    subject = f"Booking Confirmation: {booking.webinar.title}"
    message = f"Hello {booking.user.username},\n\nYou have successfully booked a spot for the webinar '{booking.webinar.title}' on {booking.webinar.date} at {booking.webinar.time}.\n\nThank you!"
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [booking.user.email],
        fail_silently=False,
    )




@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    return redirect('user_dashboard')

@login_required
def booking_confirmation_existing(request, webinar_id):
    webinar = get_object_or_404(Webinar, id=webinar_id)
    bookings = Booking.objects.filter(user=request.user, webinar=webinar, status='booked').first()
    return render(request, 'webinars/booking_confirmation_existing.html', {
        'webinar': webinar,
        'bookings': bookings,
    })

@login_required
def profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile was updated successfully!")

            return redirect('profile')  # refresh after saving
    else:
        form = EditProfileForm(instance=request.user)
    
    return render(request, 'webinars/profile.html', {'form': form})


def user_dashboard(request):
    bookings = Booking.objects.filter(user=request.user).select_related('webinar')
    return render(request, 'webinars/user_dashboard.html', {
        'bookings': bookings,
        'today': date.today()
    })



