from django.urls import path, include

from Nail_studio.user_profile.views import ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = (
    path('', include([
        path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile_details'),
        path('edit/<int:pk>/', ProfileEditView.as_view(), name='profile_edit'),
        path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile_delete'),
    ])),

)
