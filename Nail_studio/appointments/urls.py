
from django.urls import path

from Nail_studio.appointments.views import BookedAppointmentsView, ManicuristAppointmentsListView
from Nail_studio.appointments.views import booking, bookingSubmit, userPanel, userUpdate, userUpdateSubmit, staffPanel

urlpatterns = (
    path('booking', booking, name='booking'),
    path('booking-submit', bookingSubmit, name='bookingSubmit'),
    path('user-panel', userPanel, name='userPanel'),
    path('user-update/<int:pk>', userUpdate, name='userUpdate'),
    path('user-update-submit/<int:pk>', userUpdateSubmit, name='userUpdateSubmit'),
    path('staff-panel', staffPanel, name='staffPanel'),
    path('booked-appointments/', BookedAppointmentsView.as_view(), name='booked_appointments'),
    path('manicurist-appointments/', ManicuristAppointmentsListView.as_view(), name='manicurist_appointments'),
)