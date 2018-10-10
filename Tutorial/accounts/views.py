from django.urls import path, re_path, reverse_lazy
from accounts import views
from django.contrib.auth import views as auth_views

# app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    re_path(r'profile/(?P<pk>\d+)/', views.view_profile, name='view_profile_with_pk'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/password/', views.change_password, name='change_password'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html', email_template_name='accounts/reset_password_email.html', success_url=reverse_lazy('accounts:password_reset_done')), name='reset_password'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset_password_done.html'), name='password_reset_done'),
    re_path(r'reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/reset_password_confirm.html', success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_password_complete.html'), name='password_reset_complete'),
]
