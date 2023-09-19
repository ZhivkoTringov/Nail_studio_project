from django.db import models


class GalleryPhoto(models.Model):
    image_file = models.ImageField(
        upload_to='photos/',
        null=True,
        blank=True,
    )

    class Meta:
        permissions = [
            ('manage_photos', 'Can manage photos'),
        ]
