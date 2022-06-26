
from django.conf import PASSWORD_RESET_TIMEOUT_DAYS_DEPRECATED_MSG
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.shortcuts import render,redirect
from store.models.customer import Customer
from store.models.orders import Order
from store.models.product import Product
from django.views import View


class OrderView(View):
   
    def get(self,request):
        customer =request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        
        return render(request,'orders.html',{'orders':orders})