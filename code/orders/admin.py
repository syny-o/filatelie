from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
        'paid',
        'created',
        'updated',
        'fk_profile'
    ]

    # list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

    # Customize the detail (form) view
    fieldsets = (
        ('Profil', {
            'fields': ('fk_profile',)  # Add fields here for the detail view
        }),
        # You can add more sections if needed
        ('Objednavka', {
            # 'classes': ('collapse',),
            'fields': ('first_name', 'last_name', 'email', 'address', 'city', 'postal_code' ,'paid')
        }),
    ) 
    readonly_fields = ('fk_profile',)  # Make fk_profile non-editable   
