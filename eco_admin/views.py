from django.shortcuts import render

# Create your views here.
def admin_index(request):
    return render(request,'admin_templates/admin_index.html')

def admin_approvesellers(request):
    return render(request,'admin_templates/admin_approve_sellers.html')

def admin_viewsellers(request):
    return render(request,'admin_templates/admin_view_sellers.html')

def admin_viewcustomer(request):
    return render(request,'admin_templates/admin_view_customer.html')

def admin_changepassword(request):
    return render(request,'admin_templates/admin_change_password.html')