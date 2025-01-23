from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import UserRegistrationForm, ProfileForm, UserEditForm, AddressForm
from .models import Profile, Address, FavoriteProduct

from shop.models import Product



@login_required(login_url='account:login')
def dashboard(request):

    profile = request.user.profile 
    address = profile.address

    if request.method == 'GET':
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        
        address_form = AddressForm(instance=address)

        favorite_products = FavoriteProduct.objects.filter(profile=profile)
    
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'address_form': address_form,

            'favorite_products': favorite_products,

            }
        
        return render(request, 'account/dashboard.html', context)  
    

    
    
    if request.method == 'POST':
        user_form = UserEditForm(
            instance=request.user,
            data=request.POST
            )
    
        profile_form = ProfileForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES,
            )
        
        address_form = AddressForm(
            instance=address,     
            data=request.POST       
        )
        
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'address_form': address_form,
            }        
        
        if user_form.is_valid() and profile_form.is_valid() and address_form.is_valid():
            user_form.save()
            profile_form.save()
            address_form.save()

            messages.success(request, "Profil byl úspěšně aktualizován.")
            return render(request, 'account/dashboard.html', context)
        else:
            messages.error(request, "Opravte chyby ve formuláři.")
            return render(request, 'account/dashboard.html', context)


      




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():

            # 1. Create user
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])  # set_password() is secure way to save password (hashing)
            new_user.save()

            # 2. Create user profile (One to One relationship)
            user_profile = Profile.objects.create(user=new_user)

            # 3. Create user address (One to One relationship)
            Address.objects.create(profile=user_profile)

            return render(request, 'account/register_done.html', {'new_user': new_user})
        
        else:
            return HttpResponse("form is not valid")
        

    if request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'account/register.html', {'form': form})
    





def edit(request):
    if request.method == 'GET':
        user_form = UserRegistrationForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    
    
    if request.method == 'POST':
        pass

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'account/dashboard.html', context)




def toggle_favorite(request, product_id):
    product = Product.objects.get(id=product_id)
    is_favorite = False

    profile = Profile.objects.get(user=request.user)

    # Favorite products
    favorite_products = FavoriteProduct.objects.filter(profile=profile)
    favorite_products = [item.product for item in favorite_products]

    if product in favorite_products:
        product_to_delete = FavoriteProduct.objects.get(product=product, profile=profile)
        product_to_delete.delete()
    else:
        FavoriteProduct.objects.create(product=product, profile=profile)
        is_favorite = True

    # Return the updated button HTML
    return HttpResponse(render(request, 'shop/product/btn_wishlist.html', {
        'product': product,
        'is_favorite': is_favorite,
    }))
    
        
