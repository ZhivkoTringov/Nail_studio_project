from django.urls import path, include

from Nail_studio.services.views import ServiceListView, ServiceCreateView, ServiceEditView, ServiceDeleteView

urlpatterns = (
    path('', include([
        path('', ServiceListView.as_view(), name='service_list'),
        path('create/', ServiceCreateView.as_view(), name='service_create'),
        path('<int:pk>/edit/', ServiceEditView.as_view(), name='service_edit'),
        path('<int:pk>/delete/', ServiceDeleteView.as_view(), name='service_delete'),

    ])),
)