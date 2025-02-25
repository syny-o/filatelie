from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import CustomLoginForm


app_name = 'account'


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html', authentication_form=CustomLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name='password_change_done'),

    path('register/', views.register, name='register'),

    path('dashboard/', views.dashboard, name='dashboard'),
    
    
]


# htmx_urlpatterns = [
#     path('check-if-username-exists/', views.check_if_username_exists, name='check_if_username_exists'),
# ]



# urlpatterns += htmx_urlpatterns