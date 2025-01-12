from django.db import models
from django.conf import settings


DEFAULT_PHOTO = 'img/blank-profile.png'


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Datum narození')
    
    photo = models.ImageField(
        upload_to='users/%Y/%m/%d/',
        default=DEFAULT_PHOTO,
        verbose_name='Fotografie'
    )

    def __str__(self):
        return f'Profile of {self.user.username}'
    

    def delete(self, *args, **kwargs):
        if self.photo.name != DEFAULT_PHOTO:
            self.photo.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Uživatelský profil'
        verbose_name_plural = 'Uživatelské profily'
