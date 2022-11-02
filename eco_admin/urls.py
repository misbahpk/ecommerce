from django.urls import path
from . import views
app_name = 'eco_admin'

urlpatterns=[
    path('admin_index',views.admin_index,name = 'admin_index'),
    path('admin_approve_sellers',views.admin_approvesellers,name = 'admin_approvesellers'),
    path('admin_view_sellers',views.admin_viewsellers,name = 'admin_viewsellers'),
    path('admin_view_customer',views.admin_viewcustomer,name = 'admin_viewcustomer'),
    path('admin_change_password',views.admin_changepassword,name = 'admin_changepassword')
]