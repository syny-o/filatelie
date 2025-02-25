import json
from django.shortcuts import render

from shop.models import Product



def home(request):

    with open("core/data/testimonials.json", "r", encoding="utf-8") as file:
        testimonials = json.load(file)

    products = Product.objects.all().order_by('-created')[:4]

    context = {
        'products': products,
        'testimonials' : testimonials,
    }


    return render(request, 'core/home.html', context)





