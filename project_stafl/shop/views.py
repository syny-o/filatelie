from django.shortcuts import get_object_or_404, render

from .models import Category, Product


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

    print(products)
        
    
    # if category_slug:
        
    #     category = get_object_or_404(Category, slug=category_slug)
    #     products = products.filter(category=category)

        
    print(ordering_criteria)
        
    return render(
        request,
        'shop/product/list.html',
        {
            'selected_categories': selected_categories,
            'ordering_criteria': ordering_criteria,
            'all_categories': categories,
            'products': products,

        }
    )
    



def product_detail(request, id, slug):
    
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    
    return render(
            request,'shop/product/detail.html', {'product': product}
        )

