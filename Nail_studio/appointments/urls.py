
from django.urls import path

from Nail_studio.appointments.views import BookedAppointmentsView, ManicuristAppointmentsListView
from Nail_studio.appointments.views import booking

urlpatterns = (
    path('booking', booking, name='booking'),
    path('booked-appointments/', BookedAppointmentsView.as_view(), name='booked_appointments'),
    path('manicurist-appointments/', ManicuristAppointmentsListView.as_view(), name='manicurist_appointments'),
)