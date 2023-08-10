
from django.urls import path

from Nail_studio.appointments.views import BookedAppointmentsView, ManicuristAppointmentsListView, BookAppointmentView, \
    EditAppointmentView, DeleteAppointmentView

urlpatterns = (
    path('booking/', BookAppointmentView.as_view(), name='booking'),
    path('booked-appointments/<int:pk>/', BookedAppointmentsView.as_view(), name='booked_appointments'),
    path('manicurist-appointments/<int:pk>/', ManicuristAppointmentsListView.as_view(), name='manicurist_appointments'),
    path('appointments/<int:pk>/edit/', EditAppointmentView.as_view(), name='manicurist_appointments_edit'),
    path('appointments/<int:pk>/delete/', DeleteAppointmentView.as_view(), name='manicurist_appointments_delete'),
)