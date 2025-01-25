from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from django.contrib import messages

from .forms import UserRegistrationForm, ProfileForm, UserEditForm, AddressForm
from .models import Profile, Address




@login_required(login_url='account:login')
def dashboard(request):

    user = request.user
    profile = user.profile 
    address = profile.address

    if request.method == 'GET':
        user_form = UserEditForm(instance=user)
        profile_form = ProfileForm(instance=profile)        
        address_form = AddressForm(instance=address)
    
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'address_form': address_form,
            }
        
        return render(request, 'account/dashboard.html', context)  
    

    
    
    if request.method == 'POST':
        user_form = UserEditForm(
            instance=user,
            data=request.POST
            )
    
        profile_form = ProfileForm(
            instance=profile,
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






# HTMX
def check_if_username_exists(request):
    print(request.POST)
    username = request.POST.get('username').strip()

    if username:
        if get_user_model().objects.filter(username=username).exists():
            return HttpResponse("<div style='color:red'>Username already exists</div>")
        else:
            return HttpResponse("<div style='color:green'>Username is available</div>")
    else:
        return HttpResponse("<div style='color:red'>Username is required</div>")







