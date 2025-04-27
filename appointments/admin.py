from django.contrib import admin
from .models import Appointment
# Register your models here.
admin.site.register(Appointment) 
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'date', 'time', 'status')
    list_filter = ('status', 'date')
    search_fields = ('full_name', 'email', 'phone')