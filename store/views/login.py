
from django.contrib.auth.hashers import check_password
from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.views import View

class Login(View):

    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        error_message= None
        postData = request.POST
        email = postData.get('email')
        password = postData.get('password')
        customer = Customer.get_customer_by_email(email)
        
        
        if customer:
           request.session['customer'] = customer.id
          
           flag = check_password(password,customer.password)
          
           if not flag:
              error_message ="Email or Password are invalid" 
              return render(request,'login.html',{'error_message':error_message})
           else:
               return redirect('/')

        else:
            error_message ="Email or Password are invalid"
       
            return render(request,'login.html',{'error_message':error_message})
def logout(request):
    request.session.clear()
    return redirect('login')
