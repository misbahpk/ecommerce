from django.urls import path
from . import views
app_name = 'common'

urlpatterns=[
   path('',views.common_index,name = 'index'),
   path('admin_home',views.common_admin_home,name = 'admin_home'),
   path('seller_home',views.common_seller_home,name = 'seller_home'),
   path('customer_home',views.common_customer_home,name = 'customer_home')
   
]