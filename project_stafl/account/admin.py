from django.contrib import admin
from .models import Profile, Address, FavoriteProduct
from orders.models import Order


admin.site.register(Address)
admin.site.register(FavoriteProduct)


class OrderInline(admin.TabularInline):
    model = Order
    raw_id_fields = ['fk_profile']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

    inlines = [OrderInline]
    