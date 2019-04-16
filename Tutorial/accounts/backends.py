from django.contrib.auth.models import User


class EmailBackend(object):
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
        except User.MultipleObjectsReturned:
            user = User.objects.filter(email=username).order_by('id').first()
        except User.DoesNotExist:
            return None
        if getattr(user, 'is_active') and user.check_password(password):
            return user
        return None
    
    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        return user
    
class UsernameBackend(object):
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
        except User.MultipleObjectsReturned:
            user = User.objects.filter(username=username).order_by('id').first()
        except User.DoesNotExist:
            return None
        if getattr(user, 'is_active') and user.check_password(password):
            return user
        return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
