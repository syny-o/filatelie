from django.shortcuts import get_object_or_404, render, HttpResponse

from .models import Category, Product

from account.models import Profile


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    # Filter by selected categories
    selected_categories = request.GET.getlist('categories')  # Retrieve all selected categories
    ordering_criteria = request.GET.get('ordering-criteria')  # Retrieve all selected orderings
    # print(request.GET)
    if selected_categories:
        products = products.filter(category__slug__in=selected_categories)

    if ordering_criteria:
        products = products.order_by(ordering_criteria)

    # Favorite products
    wishlist = request.user.profile.wishlist.all()

    # print(products)
        
    
    # if category_slug:
        
    #     category = get_object_or_404(Category, slug=category_slug)
    #     products = products.filter(category=category)

        
    # print(ordering_criteria)
        
    return render(
        request,
        'shop/product/list.html',
        {
            'selected_categories': selected_categories,
            'ordering_criteria': ordering_criteria,
            'all_categories': categories,
            'products': products,
            'favorite_products': wishlist,

        }
    )
    



def product_detail(request, id, slug):
    
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    profile = Profile.objects.get(user=request.user)
    wishlist = profile.wishlist.all()

    is_favorite = product in wishlist
    
    return render(
            request,'shop/product/detail.html', {'product': product, 'favorite_products' : wishlist, 'is_favorite': is_favorite}
        )




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
    return HttpResponse(render(request, 'shop/product/btn_wishlist.html', {
        'product': product,
        'is_favorite': is_favorite,
    }))



def update_cart_wishlist_count(request):
    print("UPDATED WISHLIST CART")
    return HttpResponse("10")
    

