
from django.urls import path
from . import views



app_name = 'cart'



urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    # path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),

    ]

htmx_urlpatterns = [
    path('add_remove_from_cart/<int:product_id>', views.add_remove_from_cart, name='add_remove_from_cart'),
    path('refresh-cart-content', views.refresh_cart_content, name='refresh_cart_content'),

]


urlpatterns += htmx_urlpatterns