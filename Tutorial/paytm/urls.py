from django.urls import path
from paytm import views

# app_name = 'paytm'

urlpatterns = [
    path('', views.response, name='home'),
    path('payment/', views.payment, name='payment'),
    path('response/', views.response, name='response'),
]
