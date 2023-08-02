from Nail_studio.appointments.models import Appointment


def is_time_slot_available(selected_day, start_time, end_time):
    # Retrieve existing appointments for the selected day
    existing_appointments = Appointment.objects.filter(day=selected_day)

    # Check if the new appointment overlaps with any existing appointments
    for appointment in existing_appointments:
        if start_time < appointment.end_time and end_time > appointment.start_time:
            return False  # Overlapping appointment found

    return True  # No overlapping appointments found, time slot is available