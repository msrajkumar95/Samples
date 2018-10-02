from django.urls import path, re_path
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html', success_url='accounts:password_reset_done'), name='reset_password'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    re_path(r'reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/', auth_views.PasswordResetConfirmView.as_view(success_url='accounts:password_reset_complete'), name='password_reset_confirm'),
]
# {'post_reset_redirect': 'accounts:password_reset_done'}, 