from django.shortcuts import render

# Create your views here.
def common_index(request):
    return render(request,'common_templates/index.html')

def common_admin_home(request):
    return render(request,'common_templates/admin_home.html')

def common_seller_home(request):
    return render(request,'common_templates/seller_home.html')

def common_customer_home(request):
    return render(request,'common_templates/customer_home.html')

