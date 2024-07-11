from django.contrib.auth import admin, views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import (
    admin_add_product_view,
    admin_dashboard_view,
    admin_products_view,
    admin_view_booking_view,
    afterlogin_view,
    add_to_cart_view,
    cart_view,
    customer_address_view,
    home_view,
    customer_address_view,
    customer_home_view,
    customer_signup_view,
    delete_order_view,
    delete_product_view,
    download_invoice_view,
    edit_profile_view,
    my_order_view,
    my_profile_view,
    payment_success_view,
    remove_from_cart_view,
    search_view,
    update_order_view,
    update_product_view,
    dashboard,
    adminclick_view,
    admin_view_booking_view,
)

urlpatterns = [
path('', home_view, name=''),
path('afterlogin', afterlogin_view, name='afterlogin'),
path('logout', LogoutView.as_view(template_name='ecom/v2/logout/logout.html'), name='logout'),
path('dashboard', dashboard),
path('search',  search_view, name='search'),

path('adminclick',  adminclick_view),
path('adminlogin', LoginView.as_view(template_name='ecom/v2/login/admin_login.html'), name='adminlogin'),
path('admin-dashboard',  admin_dashboard_view, name='admin-dashboard'),

path('admin-products',  admin_products_view, name='admin-products'),
path('admin-add-product',  admin_add_product_view, name='admin-add-product'),
path('delete-product/<int:pk>',  delete_product_view, name='delete-product'),
path('update-product/<int:pk>',  update_product_view, name='update-product'),

path('admin-view-booking',  admin_view_booking_view, name='admin-view-booking'),
path('delete-order/<int:pk>',  delete_order_view, name='delete-order'),
path('update-order/<int:pk>',  update_order_view, name='update-order'),

path('customersignup',  customer_signup_view),
path('customerlogin', LoginView.as_view(template_name='ecom/v2/login/customer_login.html'), name='customerlogin'),
path('customer-home',  customer_home_view, name='customer-home'),
path('my-order',  my_order_view, name='my-order'),
path('my-profile',  my_profile_view, name='my-profile'),
path('edit-profile',  edit_profile_view, name='edit-profile'),
path('download-invoice/<int:orderID>/<int:productID>',  download_invoice_view, name='download-invoice'),

path('add-to-cart/<int:pk>',  add_to_cart_view, name='add-to-cart'),
path('cart',  cart_view, name='cart'),
path('remove-from-cart/<int:pk>',  remove_from_cart_view, name='remove-from-cart'),
path('customer-address',  customer_address_view, name='customer-address'),
path('payment-success',  payment_success_view, name='payment-success')]
