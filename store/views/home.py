
from django.http import HttpResponse
from django.shortcuts import redirect, render
from store.models.customer import Customer
from store.models.category import Category
from store.models.product import Product
from django.views import View

# Create your views here.

class Index(View):
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}


        products = None
        # request.session.clear
        categories = Category.get_all_categories();

        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_product_by_category_id(categoryID);
            context = {'products':products,'categories':categories}
            return render(request,'home.html',context)
        else:
            products = Product.get_all_products();
            context = {'products':products,'categories':categories}
            return render(request,'home.html',context)
    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity==1:
                        cart.pop(product)
                    else:
                     cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart ={}
            cart[product] = 1

        request.session['cart'] = cart
        return redirect("homepage")

   






        




        
        
      
        
        
        
       