from django.shortcuts import render

# Create your views here.
def customer_home(request):
    return render(request,'customer_templates/home.html')

def customer_cart(request):
    return render(request,'customer_templates/cart.html')