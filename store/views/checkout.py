
from django.conf import PASSWORD_RESET_TIMEOUT_DAYS_DEPRECATED_MSG
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.shortcuts import render,redirect
from store.models.customer import Customer
from store.models.orders import Order
from store.models.product import Product
from django.views import View

class Checkout(View):

    def post(self,request):
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

      
        for product in products:
            order = Order(customer = Customer(id = customer),
            product = product,
            price = product.price,
            phone = phone,
            address = address, 
            quantity = cart.get(str(product.id)))

            order.save()

            request.session['cart'] ={}
        return redirect('cart')
   
