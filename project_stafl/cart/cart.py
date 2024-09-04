from decimal import Decimal
from django.conf import settings

from shop.models import Product



class Cart:
    """
    You will build your cart dictionary with product IDs as keys, and for each product key, 
    a dictionary will be a value that includes quantity and price. By doing this, you can 
    guarantee that a product will not be added more than once to the cart.
    """

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    
    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True        


    
    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        
        else:
            self.cart[product_id]['quantity'] += quantity
        
        self.save()



    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)

        if product_id in self.cart:            
            del self.cart[product_id]            
            self.save()        




