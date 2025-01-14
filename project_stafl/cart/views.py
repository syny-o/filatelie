from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse, JsonResponse
from django.urls import reverse, resolve


from .cart import Cart
from shop.models import Product


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})



# @require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.add(
        product=product,
        )
    
    # return redirect('cart:cart_detail')
    
    return redirect('shop:product_detail', product.id, product.slug)


# @require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    # return redirect('cart:cart_detail')

    return redirect('shop:product_detail', product.id, product.slug)
