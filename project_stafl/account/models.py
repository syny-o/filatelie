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



    

# Address model to store one address to each user
class Address(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE
    )
    street = models.CharField(blank=True, null=True, max_length=255, verbose_name='Ulice',)
    city = models.CharField(blank=True, null=True, max_length=255, verbose_name='Město')
    state = models.CharField(blank=True, null=True, max_length=255, verbose_name='Stát')
    postal_code = models.CharField(blank=True, null=True, max_length=20, verbose_name='PSČ')
    country = models.CharField(blank=True, null=True, max_length=255, verbose_name='Země')

    def __str__(self):
        return f'Address of {self.profile.user.username}'

    class Meta:
        verbose_name = 'Adresa'
        verbose_name_plural = 'Adresy'
