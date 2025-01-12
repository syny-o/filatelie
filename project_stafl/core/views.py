from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'core/home.html')





