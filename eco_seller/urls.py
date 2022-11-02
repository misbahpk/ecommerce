from django.urls import path
from . import views
app_name = 'eco_seller'

urlpatterns=[
    path('seller_index',views.seller_index,name = 'seller_index'),
    path('seller_add_product',views.seller_addproduct,name = 'seller_addproduct'),
    path('seller_product_catalogue',views.seller_productcatalogue,name = 'seller_productcatalogue'),
    path('seller_order',views.seller_order,name = 'seller_order'),
    path('seller_stock',views.seller_stock,name = 'seller_stock'),
    path('seller_change_password',views.seller_changepassword,name = 'seller_changepassword'),
    path('seller_profile',views.seller_profile,name = 'seller_profile')
]