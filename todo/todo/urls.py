from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from todo.views import ToDoListView, ToDoDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', TemplateView.as_view(template_name='todo/index.html')),
	re_path(r'^todo/api/$', ToDoListView.as_view()),
    re_path(r'^todo/api/(?P<pk>[0-9]+)/$', ToDoDetailView.as_view()),
]
