# Generated by Django 5.1.3 on 2025-06-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webinars', '0010_alter_booking_status_alter_booking_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='booked', max_length=20),
        ),
    ]
