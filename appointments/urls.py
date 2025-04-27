from django.urls import path
from .views import book_appointment, appointment_success, appointment_list , admin_dashboard,update_status,logout_view


urlpatterns = [
    path('book/', book_appointment, name='book_appointment'),
    path('success/', appointment_success, name='appointment_success'),
    path('list/', appointment_list, name='appointment_list'),
    path('admin/', admin_dashboard, name='admin_dashboard'),
    path('update-status/<int:appointment_id>/', update_status, name='update_status'),
    path('logout/', logout_view, name='logout')
]
