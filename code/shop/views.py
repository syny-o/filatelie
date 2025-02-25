from django.shortcuts import get_object_or_404, render, HttpResponse
from django.db.models import Q
from django.views.decorators.http import require_POST

from .models import Category, Product

from account.models import Profile

from cart.cart import Cart


def product_list(request, category_slug=None):
    # category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)


    # Favorite products
    wishlist = request.user.profile.wishlist.all()

    
    # if category_slug:
        
    #     category = get_object_or_404(Category, slug=category_slug)
    #     products = products.filter(category=category)

        

        
    return render(
        request,
        'shop/product/list.html',
        {
            'all_categories': categories,
            'products': products,
            'favorite_products': wishlist,

        }
    )
    



def product_detail(request, id, slug):
    
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    profile = Profile.objects.get(user=request.user)
    wishlist = profile.wishlist.all()
    cart = Cart(request)

    is_favorite = product in wishlist
    is_in_cart = product in cart
    
    return render(
            request,'shop/product/detail.html', {'product': product, 'favorite_products' : wishlist, 'is_favorite': is_favorite, 'is_in_cart': is_in_cart}
        )




#################################################
# HTMX
#################################################


def toggle_favorite(request, product_id):
    product = Product.objects.get(id=product_id)
    profile = Profile.objects.get(user=request.user)
    
    if product in profile.wishlist.all():
        profile.wishlist.remove(product)
        is_favorite = False
    else:
        profile.wishlist.add(product)
        is_favorite = True

    # Return the updated button HTML
    return HttpResponse(render(request, 'shop/product/partials/btn_wishlist.html', {
        'product': product,
        'is_favorite': is_favorite,
    }))



@require_POST
def product_filter(request):
    
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    # Filter by selected categories
    searched_text = request.POST.get('searched-text')  # Retrieve all selected categories
    selected_categories = request.POST.getlist('categories')  # Retrieve all selected categories
    ordering_criteria = request.POST.get('ordering-criteria')  # Retrieve all selected orderings
    price_ranges = request.POST.getlist('price-ranges')  # Retrieve all selected price ranges
    

    
    if searched_text and len(searched_text)>0:
        products = products.filter(name__icontains=searched_text)

    if selected_categories:
        products = products.filter(category__slug__in=selected_categories)

    if ordering_criteria:
        products = products.order_by(ordering_criteria)

    if price_ranges:
        # Initialize a combined Q object for flexible querying        
        price_query = Q()

        # Iterate over the price range values and build the query
        for price_range in price_ranges:
            if price_range == '<1000':
                price_query |= Q(price__lt=1000)
            elif price_range == '>=1000':
                price_query |= Q(price__gte=1000)

        # Apply the combined price filter
        products = products.filter(price_query)

    

    # Favorite products
    wishlist = request.user.profile.wishlist.all()

    # print(request.POST)

        
    return render(
        request,
        'shop/product/partials/cards.html',
        {
            'selected_categories': selected_categories,
            'ordering_criteria': ordering_criteria,
            'all_categories': categories,
            'products': products,
            'favorite_products': wishlist,

        }
    )
    






    

