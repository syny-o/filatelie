from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse


from .cart import Cart
from shop.models import Product



def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})



# @require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')






###############################################################
# HTMX VIEWS:
###############################################################

def add_remove_from_cart(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    
    if product in cart:
        cart.remove(product)
        is_in_cart = False
    else:
        cart.add(product=product)
        is_in_cart = True

    # Return the updated button HTML
    return HttpResponse(render(request, 'shop/product/partials/btn_cart.html', {
        'product': product,
        'is_in_cart': is_in_cart,
    }))



def refresh_cart_content(request):
    cart = Cart(request)
    return render(request, 'cart/partials/items.html', {'cart': cart})

