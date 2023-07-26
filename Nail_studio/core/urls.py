from django.urls import path

from Nail_studio.core.views import IndexView

urlpatterns = (
 path('', IndexView.as_view(), name='index'),

)