from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import UserRegistrationForm, ProfileForm, UserEditForm



@login_required(login_url='login')
def dashboard(request):

    if request.method == 'GET':
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
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
            files=request.FILES
            )
        
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            }        
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profil byl úspěšně aktualizován.")
            return render(request, 'account/dashboard.html', context)
        else:
            messages.error(request, "Opravte chyby ve formuláři.")
            return render(request, 'account/dashboard.html', context)


      




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])  # set_password() is secure way to save password (hashing)
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
        

    if request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'account/register.html', {'user_form': form})
    


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
    
        
