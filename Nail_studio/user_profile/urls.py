from django.urls import path

from Nail_studio.user_profile.views import ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = (
    path('', ProfileDetailsView.as_view(), name='profile details'),
    path('edit/', ProfileEditView.as_view(), name='profile edit'),
    path('delete/', ProfileDeleteView.as_view(), name='profile delete'),

)