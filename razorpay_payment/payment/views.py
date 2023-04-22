from django.shortcuts import render
import razorpay
from . import models
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = int(request.POST.get("amount")) * 100
        print(name)
        print(amount)
        razorpay_client = razorpay.Client(auth=("rzp_test_X37P2XdPEZR3gI", "hdOGYFTyrqonMepAuiAVYavQ"))
        payment = razorpay_client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
        print(payment)
        razor =models.Razor(name = name, amount = amount, payment_id = payment['id'])
        razor.save()
        return render(request, 'index.html', {'payment':payment})
    return render(request, 'index.html')

@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break
        user = models.Razor.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()    
    return render(request, 'success.html')