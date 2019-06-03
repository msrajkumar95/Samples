from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from todo.views import ToDoView

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', TemplateView.as_view(template_name='todo/index.html')),
	path('todo/api/', ToDoView.as_view()),
]
