from django.contrib import admin
from paytm.models import PaymentHistory
# Register your models here.
class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'MID', 'TXNAMOUNT', 'STATUS')


admin.site.register(PaymentHistory, PaymentHistoryAdmin)