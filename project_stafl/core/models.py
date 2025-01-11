from django.db import models
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorie'

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])




class Product(models.Model):
    # Kategorie, do které produkt patří - vztah k modelu Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'



    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])


