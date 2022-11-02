from django.urls import path
from . import views
app_name = 'eco_customer'

urlpatterns=[
    path('eco_customer_index',views.eco_customer_index,name= 'eco_index'),
    path('eco_customer_profile',views.eco_customer_profile,name = 'eco_profile'),
    path('eco_customer_product',views.eco_customer_product,name = 'eco_product'),
    path('eco_customer_cart',views.eco_customer_cart,name = 'eco_cart'),
    path('eco_customer_change_password',views.eco_customer_changepassword,name = 'eco_password'),
    path('eco_customer_orders',views.eco_customer_orders,name = 'eco_orders')
]