from django.urls import path

from Nail_studio.core.views import IndexView, ServiceListView

urlpatterns = (
 path('', IndexView.as_view(), name='index'),

)