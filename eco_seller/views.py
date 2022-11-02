from django.shortcuts import render

# Create your views here.
def seller_index(request):
    return render(request,'seller_templates/seller_index.html')

def seller_addproduct(request):
    return render(request,'seller_templates/seller_add_product.html')

def seller_productcatalogue(request):
    return render(request,'seller_templates/seller_product_catalogue.html')

def seller_order(request):
    return render(request,'seller_templates/seller_order.html')

def seller_stock(request):
    return render(request,'seller_templates/seller_stock.html')

def seller_changepassword(request):
    return render(request,'seller_templates/seller_change_password.html')

def seller_profile(request):
    return render(request,'seller_templates/seller_profile.html')

