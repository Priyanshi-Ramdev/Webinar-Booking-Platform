from django.db import models
from django.contrib.auth.models import User

class Webinar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    speaker_name = models.CharField(max_length=100)
    speaker_bio = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    duration_minutes = models.PositiveIntegerField()
    image = models.ImageField(upload_to='webinar_images/', blank=True, null=True)
    category = models.CharField(max_length=100, choices=[
        ('tech', 'Technology'),
        ('marketing', 'Marketing'),
        ('business', 'Business'),
        ('design', 'Design'),
        ('health', 'Health'),
    ])
    meet_link = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.title




class Booking(models.Model):
    STATUS_CHOICES = (
        ('booked', 'Booked'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    webinar = models.ForeignKey("Webinar", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="anonymous")
    email = models.EmailField(default="default@example.com")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='booked')  # ✅ Add this
    
    class Meta:
        unique_together = ('user', 'webinar')

    def __str__(self):
        return f"{self.name} - {self.webinar.title} ({self.status})"

