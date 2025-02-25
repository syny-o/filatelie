
from django.urls import path
from . import views



app_name = 'shop'



urlpatterns = [
    path('', views.product_list, name='product_list'),

    path(
        '<slug:category_slug>/',
        views.product_list,
        name='product_list_by_category'
        ),
    
    path(
        '<int:id>/<slug:slug>/',
        views.product_detail,
        name='product_detail'
        ),
    
    path(
        'toggle-favorite/<int:product_id>', 
        views.toggle_favorite, 
        name='toggle_favorite'),

    ]


htmx_urlpatterns = [
    path('product-filter', views.product_filter, name='product_filter'),
]


urlpatterns += htmx_urlpatterns