from django.contrib import admin
from quickstart.models import Snippet

# Register your models here.
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'code', 'language', 'style')
    
    def get_queryset(self, request):
        queryset = super(SnippetAdmin, self).get_queryset(request)
        return queryset

    
admin.site.register(Snippet, SnippetAdmin)