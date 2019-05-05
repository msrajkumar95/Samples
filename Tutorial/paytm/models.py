from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PaymentHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_payment_paytm')
    ORDERID = models.CharField('ORDER ID', max_length=30)
    TXNDATE = models.DateTimeField('TXN DATE', auto_now_add=True)
    TXNID = models.CharField('TXN ID', max_length=64)
    BANKTXNID = models.CharField('BANK TXN ID', max_length=20, null=True, blank=True)
    BANKNAME = models.CharField('BANK NAME', max_length=50, null=True, blank=True)
    RESPCODE = models.IntegerField('RESP CODE')
    PAYMENTMODE = models.CharField('PAYMENT MODE', max_length=10, null=True, blank=True)
    CURRENCY = models.CharField('CURRENCY', max_length=4, null=True, blank=True)
    GATEWAYNAME = models.CharField('GATEWAY NAME', max_length=30, null=True, blank=True)
    MID = models.CharField(max_length=40)
    RESPMSG = models.TextField('RESP MSG', max_length=250)
    TXNAMOUNT = models.FloatField('TXN AMOUNT')
    STATUS = models.CharField('STATUS', max_length=12)

    class Meta:
        app_label = 'paytm'

    def __unicode__(self):
        return self.STATUS