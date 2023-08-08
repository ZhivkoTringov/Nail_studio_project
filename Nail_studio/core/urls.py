from django.urls import path

from Nail_studio.core.views import IndexView, AboutView, ContactUsView

urlpatterns = (
 path('', IndexView.as_view(), name='index'),
 path('about/', AboutView.as_view(), name='about'),
 path('contact/', ContactUsView.as_view(), name='contact'),

)