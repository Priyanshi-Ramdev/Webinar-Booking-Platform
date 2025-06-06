"""
URL configuration for webinar_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from webinars import views
from django.contrib.auth.views import LogoutView, LoginView
from webinars import views as webinar_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webinars.urls')),  
    path('webinars/<int:webinar_id>/', views.webinar_detail, name='webinar_detail'),  # Webinar details page
    path('booking_confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),  # Booking confirmation page
    path('', webinar_views.homepage, name='homepage'),  # This links the root URL to the homepage view
    path('accounts/', include('django.contrib.auth.urls')),

    path('profile/', views.profile, name='profile'),
    path('', views.homepage, name='homepage'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)