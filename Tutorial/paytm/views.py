from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from paytm import checksum
from paytm.models import PaymentHistory
# Create your views here.

@login_required
def payment(request):
    CALLBACK_URL = settings.HOST_URL + settings.PAYTM_CALLBACK_URL
    # Generating unique temporary ids
    order_id = checksum.__id_generator__()

    bill_amount = request.POST['amount']
    if bill_amount:
        data_dict = {
                    'MID':settings.PAYTM_MERCHANT_ID,
                    'ORDER_ID':order_id,
                    'TXN_AMOUNT': bill_amount,
                    'CUST_ID':request.user.email,
                    'INDUSTRY_TYPE_ID':settings.PAYTM_INDUSTRY_TYPE,
                    'WEBSITE': settings.PAYTM_WEBSITE,
                    'CHANNEL_ID':'WEB',
                    'CALLBACK_URL':CALLBACK_URL,
                }
        param_dict = data_dict
        param_dict['CHECKSUMHASH'] = checksum.generate_checksum(data_dict, settings.PAYTM_MERCHANT_KEY)
        return render(request,"paytm/payment.html",{'paytmdict':param_dict})
    return HttpResponse("Bill Amount Could not find. ?bill_amount=10")

@login_required
@csrf_exempt
def response(request):
    if request.method == 'GET':
        return render(request, 'paytm/home.html')
    elif request.method == "POST":
        data_dict = {}
        for key in request.POST:
            data_dict[key] = request.POST[key]
        verify = checksum.verify_checksum(data_dict, settings.PAYTM_MERCHANT_KEY, data_dict['CHECKSUMHASH'])
        if verify:
            for key in request.POST:
                if key == "BANKTXNID" or key == "RESPCODE":
                    if request.POST[key]:
                        data_dict[key] = int(request.POST[key])
                    else:
                        data_dict[key] = 0
                elif key == "TXNAMOUNT":
                    data_dict[key] = float(request.POST[key])
            PaymentHistory.objects.create(user=request.user, **data_dict)
            return render(request,"paytm/response.html",{"paytm":data_dict})
        else:
            return HttpResponse("checksum verify failed")
    return HttpResponse(status=200)