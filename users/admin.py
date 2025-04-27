from django.contrib import admin
from .models import Profile

# Extend UserAdmin to display Profile information
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')  # Show these fields in the admin panel

admin.site.register(Profile, ProfileAdmin)  # Register Profile with ProfileAdmi

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'status')  # Show appointments
    list_filter = ('status', 'date')
    search_fields = ('user__username', 'user__email')
