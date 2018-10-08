from django.urls import path, re_path
from home import views

# app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    re_path(r'friend/(?P<operation>.+)/(?P<pk>\d+)/', views.change_friends, name='change_friend')
]
