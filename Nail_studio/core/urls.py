from django.urls import path

from Nail_studio.core.views import IndexView, AboutView, ContactView, GalleryView, UploadPhotoView, DeletePhotoView

urlpatterns = (
 path('', IndexView.as_view(), name='index'),
 path('about/', AboutView.as_view(), name='about'),
 path('contact/', ContactView.as_view(), name='contact'),
 path('gallery/', GalleryView.as_view(), name='gallery'),
 path('gallery/upload-photo/', UploadPhotoView.as_view(), name='upload_photo'),
 path('gallery/delete-photo/<int:pk>/', DeletePhotoView.as_view(), name='delete_photo'),

)