from django.shortcuts import render

# Create your views here.
def eco_customer_index(request):
    return render(request,'eco_customer_templates/customer_index.html')

def eco_customer_profile(request):
    return render(request,'eco_customer_templates/customer_profile.html')

def eco_customer_product(request):
    return render(request,'eco_customer_templates/customer_product.html')

def eco_customer_cart(request):
    return render(request,'eco_customer_templates/customer_cart.html')

def eco_customer_changepassword(request):
    return render(request,'eco_customer_templates/customer_change_password.html')

def eco_customer_orders(request):
    return render(request,'eco_customer_templates/customer_orders.html')