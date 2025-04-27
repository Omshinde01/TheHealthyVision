from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Appointment
from .forms import AppointmentForm
from django.contrib.auth import logout

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user  # Link appointment to the logged-in user
            appointment.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    
    return render(request, 'appointments/book_appointment.html', {'form': form})

@login_required
def appointment_success(request):
    return render(request, 'appointments/appointment_success.html')

@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

# views.py

def logout_view(request):
    logout(request)
    return redirect('home')

@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    appointments = Appointment.objects.all().order_by('-date', '-time')
    return render(request, 'appointments/admin_dashboard.html', {'appointments': appointments})

@user_passes_test(lambda u: u.is_staff)
def update_status(request, appointment_id):
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, id=appointment_id)
        new_status = request.POST.get('status')
        if new_status in ['Pending', 'Confirmed', 'Cancelled']:
            appointment.status = new_status
            appointment.save()
    return redirect(admin_dashboard)