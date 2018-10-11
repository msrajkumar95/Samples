from django.contrib import admin
from home.models import Friend, Post

# Register your models here.
class FriendAdmin(admin.ModelAdmin):
    list_display = ('user', 'friends')
    
    def user(self, obj):
        friends = Friend.objects.get(current_user=obj.current_user)
        return str(obj.current_user) + ' (' + str(len(friends.users.all())) + ')'
    
    def friends(self, obj):
        friends_list = [ user.username for user in Friend.objects.get(current_user=obj.current_user).users.all()]
        friends_list.sort()
        return friends_list
    
    def get_queryset(self, request):
        queryset = super(FriendAdmin, self).get_queryset(request)
        queryset = queryset.order_by('current_user')
        return queryset
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('post', 'created_by', 'created_on', 'updated_on')
     
    def created_by(self, obj):
        return obj.user
    
    def created_on(self, obj):
        return obj.created
    
    def updated_on(self, obj):
        return obj.updated
     
    def get_queryset(self, request):
        queryset = super(PostAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-created', '-updated')
        return queryset
 
admin.site.register(Friend, FriendAdmin)
admin.site.register(Post, PostAdmin)
