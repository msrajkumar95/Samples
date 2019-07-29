from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from todo.views import ToDoListView, ToDoDetailView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='ToDo API')

urlpatterns = [
    path('admin', admin.site.urls),
	path('', TemplateView.as_view(template_name='todo/index.html')),
	path('docs', schema_view),
	path('api/todo', ToDoListView.as_view()),
    path('api/todo/<int:pk>', ToDoDetailView.as_view()),
]
