from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

handler404 = 'Nail_studio.core.views.custom_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Nail_studio.core.urls')),
    path('appointments/', include('Nail_studio.appointments.urls')),
    path('auth/', include('Nail_studio.users_auth.urls')),
    path('services/', include('Nail_studio.services.urls')),
    path('profile/', include('Nail_studio.user_profile.urls')),
    path('booking/', include('Nail_studio.appointments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)