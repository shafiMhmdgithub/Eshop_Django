from django.contrib.auth.hashers import make_password
from django.shortcuts import render,redirect
from store.models.customer import Customer

from django.views import View


class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        values = {
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email}
        #validation
        error_message = None
        customer = Customer(first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password)
    
        error_message =self.validateUser(customer)
        #saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('/')
        else:
            data ={
                'error_message':error_message,
                'values':values}
            
            return render(request, 'signup.html',data)

    def validateUser(self,customer):
        error_message = None
        if(not customer.first_name):
            error_message = "First name required"
        elif len(customer.first_name)<3:
                error_message ="Name must be greater than 4 Characters"
        elif(not customer.last_name):
            error_message = "last name required"
        elif len(customer.last_name)<4:
                error_message =" Last Name must be greater than 4 Characters"
        elif(not customer.phone):
            error_message = "phone number is required"
        elif len(customer.phone)<6:
                error_message ="Phone Number greater than 4 Characters"
        elif(not customer.password):
            error_message = "password is required"
        elif len(customer.password)<4:
                error_message ="password must be greater than 4 Characters"
        elif len(customer.email)<4:
            error_message = "Email must be greater "
        elif customer.isExists():
            error_message = 'Email address is already Registered'

        return error_message

