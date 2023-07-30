
from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('Nail_studio.core.urls')),
    path('appointments/', include('Nail_studio.appointments.urls')),
    path('auth/', include('Nail_studio.users_auth.urls')),
    path('services/', include('Nail_studio.services.urls')),
    path('profile/', include('Nail_studio.user_profile.urls')),
    path('booking/', include('Nail_studio.appointments.urls')),

)
