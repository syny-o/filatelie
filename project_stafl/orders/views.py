from django.shortcuts import render

from .models import Order, OrderItem
from .forms import OrderForm

from cart.cart import Cart



def summary(request):
    user = request.user


    if request.method == 'GET':
        if user.is_authenticated:
            form = OrderForm(initial={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'address': request.user.profile.address.street,
                'postal_code': request.user.profile.address.postal_code,
                'city': request.user.profile.address.city,
            })

        else:
            form = OrderForm()
    
        return render(request, 'orders/summary.html', {'form': form})

    
    if request.method == 'POST':
        cart = Cart(request)

        form = OrderForm(request.POST)
        
        if form.is_valid():
            order = form.save()
            # create order items from cart
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                    )
            
            # clear the cart
            cart.clear()

            return render(request, 'orders/summary.html')
    

    