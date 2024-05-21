from ast import Add, Delete
import email
from math import prod
from pickle import INST
from tabnanny import check
from django.conf import settings

from django.db.models import query
from MyApp.form import Product
from django.shortcuts import render
from django.shortcuts import redirect
from MyApp.models import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate, login, logout 
from django.core.mail import send_mail



def home(request):
    return render(request,'home.html')

def logout1(request):
    logout(request)
    return redirect(ind2)

# Create your views here.
def ind1(request):
    prodlist=AddProduct.objects.all()
    return render(request,'index.html',{'prod1':prodlist})

#def login(request):
 # if request.method=='POST':
      #email1=request.POST.get('email')
      #pass1=request.POST.get('password')
     #+ print(pass1)
     # check with database
     # user=users.objects.get(Email=email1)
      #admin=adminData.objects.get(Email=email1)
      #print(user.Password)
      #if user:
          #print(check_password(pass1,user.Password))
          #print(user.Password)
         #if check_password(pass1,user.Password):
           
              #request.session['name']=user.Name
              #request.session['email']=user.Email
              #return render(request,"index_2.html")
         #else:
              #  message="password does not match"
               # return render(request,"login.html",{'msg':message})
    #  else:
         # message="user does not exist"
          #return render(request,"registration.html",{'msg':message})
  #else:
      # print("Error in data Submission")      
       #return render(request,'login.html')
  
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if the credentials match an admin user
        try:
            admin_user = adminData.objects.get(Email=email)
            if admin_user.Password == password:
                request.session['admin'] = admin_user.Username
                # Admin authentication successful, redirect to addproduct.html
                return redirect(add) 
        except adminData.DoesNotExist:
            pass  # Continue to check regular users
        
        # Check if the credentials match a regular user
        try:
            regular_user = users.objects.get(Email=email)
            if check_password(password, regular_user.Password):
                # Regular user authentication successful, set session variables and redirect
                request.session['name'] = regular_user.Name
                request.session['email'] = regular_user.Email
                return redirect(ind2)
            else:
                message = "Password does not match"
                return render(request, "login.html", {'msg': message})
        except users.DoesNotExist:
            message = "User does not exist"
            return render(request, "registration.html", {'msg': message})
    else:
        print("Error in data submission")
        return render(request, 'login.html')
    
def registration(request):
    if request.method=='POST':
        name1=request.POST.get('Username')
        email1=request.POST.get('email')
        password1=request.POST.get('password')
        confirmpass1=request.POST.get('confirm password')
        ph = request.POST.get('phone')
        user=users.objects.filter(Email=email1)#user already exists ot not
        if user:
            message='user already exist'
            return render(request,'login.html',{'msg':message})
        else:
            if password1==confirmpass1:
                newuser=users.objects.create(Name=name1,Email=email1,Password=make_password(password1),Phone = ph)
                message='user register successfully'
                return redirect(login)
            else:
                message='password and confirmpassword are not matching '
                return render(request,'register.html',{'msg':message})
        #Subject='Welcome to fresh fruits'
        #send_mail(Subject,'Thank you for visiting our website',settings.EMAIL_HOST_USER,[email1])
    else:
        print("Error in data Submission")
    return render(request, "register.html")

#def login(request):
 #   if request.method=='POST':
 #       email1=request.POST.get('email')
  #      pass1=request.POST.get('password')
  #      user = authenticate(request, Email=email1, Password=pass1)
  #      if user:
            
  #          try:
  #             login(request, user)    
   #            return redirect('ind2')
   #         except Exception as e:                     
   #             print("_____________All exception__________________",e) 
            
   #     else:
   #         logout(request)
    #        return render(request, 'register.html')
        
    #else:
  #      print("Error in data Submission")      
  #  return render(request,'login.html')
def ind2(request):
    prodlist=AddProduct.objects.all()
    return render(request,'index_2.html',{'prod2':prodlist})

def sho(request):
    prodlist =AddProduct.objects.all()
    #print(prodlist)
    proddict = {'prod':prodlist}
    #print(proddict)
    return render(request,'shop.html',context=proddict)
    
def abt(request):
    return render(request,'about.html')

def cart(request):
    user1=users.objects.get(Email=request.session['email'])
    cartitems=CartItem.objects.filter(user=user1)
    total_price=sum(item.product.SalePrice * item.quantity for item in cartitems)
    return render(request,'cart.html',{'cart_items':cartitems,'total_price':total_price})


def decrease_quantity(request, product_id):
    cart_item = CartItem.objects.get(product__ProductId=product_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect(cart)

def increase_quantity(request, product_id):
    cart_item = CartItem.objects.get(product__ProductId=product_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect(cart)



def view(request):
    return render(request,'views.html')


#def cheout(request):
  #  return render(request,'checkout.html')
def detail(request,pk=3):
    product=ProductDescip.objects.filter(Product=pk)
    prodlist=ProductDescip.objects.all()
    print(product)
    return render(request,'single-product.html',{'product':product, 'prod':prodlist})

def sproduct(request):
    prodlist=ProductDescip.objects.all()
    return render(request,'single-product.html',{'prod':prodlist})


def snews(request):
    return render(request,'single-news.html')


def file404(request):
    return render(request,'404.html')

def news(request):
    return render(request,'news.html')
    
def submitQuary(request):
    if request.method=="POST":
        contacts = contactQuary()
        contacts.Name=request.POST.get('name')
        contacts.Email=request.POST.get('email')
        contacts.Phone=request.POST.get('phone')
        contacts.Subject=request.POST.get('subject')
        contacts.Message=request.POST.get('message')
        send_mail("Fresh Fruits",'Thank you for visiting our website. Keep shoping',settings.EMAIL_HOST_USER,[contacts.Email])
        contacts.save()
        return redirect(ind1)
    else:
        print("Error in data Submission")
        
    return render(request,"contact.html")

def cheout(request):
    if request.method=='POST':
        user=UserDetails()
        user.Name=request.POST.get('name')
        user.Email=request.POST.get('email')
        user.Phone=request.POST.get('phone')
        user.Address=request.POST.get('address')
        user.Message=request.POST.get('bill')
        
        user.save()
        return redirect(ind2)
    else:
        print("Error!")
    user1=users.objects.get(Email=request.session['email'])
    cartitems=CartItem.objects.filter(user=user1)
    total_price=sum(item.product.SalePrice * item.quantity for item in cartitems)
    return render(request,'checkout.html',{'cart_items':cartitems,'total_price':total_price})
   

#def add(request):
#	form = Product()
#	if request.method == 'POST':
		
#		form = Product(request.POST)

#		if form.is_valid():
#			form.save()
#			return ind2(request)
#		else:
#			print("Error in data Submission")
#	return render(request,'addproduct.html', {'form': form})
#def show_product(request):
#    prodlist =AddProduct.objects.all()
 #   proddict = {'prod':prodlist}
#    return render(request,'showProduct.html',context=proddict)

def add(request):
    
    if request.method=="POST":
        form  = Product(request.POST,request.FILES or None)
        if form.is_valid():
            form.save()
            return add(request)
        else:
            print("error in data submission")
    
    productlist = AddProduct.objects.all()
    form = Product()
    return render(request, "addproduct.html",{'form':form, 'product':productlist})

def DeleteData(request,pk):
    deldata=AddProduct.objects.get(ProductId=pk)
    deldata.delete()
    return redirect(add)

def delprod(request,pk):
    delproduct=AddProduct.objects.get(ProductId=pk)
    delproduct.delete()
    return redirect(cart)

def updatedata(request,pk=0):
      prod = AddProduct.objects.get(ProductId=pk)
      form=Product(request.POST or None,request.FILES or None,instance=prod)
      
      if form.is_valid():
          AddProduct.objects.filter(ProductId=pk).update(ProductId=prod.ProductId)
          form.save()
          return redirect(add)
      else:
          for field in form:
              print("Field error: ",field.name,field.errors)
              
      productlist = AddProduct.objects.all()      
      return render(request,'updateproduct.html',{'form':form,'product':productlist})


def add_to_cart(request,product_id):
    #print("bvvvvvvvvbvb")
    product1=AddProduct.objects.get(ProductId=product_id)
    user1 = users.objects.get(Email = request.session['email'])
    cart_item,created=CartItem.objects.get_or_create(product=product1,user=user1)   
    if request.method =='GET':
        quanti=request.GET.get('quant')
        #print("____________________",quanti)
        if quanti is not None:
            cart_item.quantity +=quanti
        else:
            cart_item.quantity +=1
    cart_item.save()
    return redirect(sho)

def search(request):
    if request.method=='GET':
        Query=request.GET.get('query')
       # print(Query)
        if Query:
            products=AddProduct.objects.filter(ProductName__icontains=Query)
            if products:
              print(products)
              return render(request,'search.html',{'prod':products})
            else:
              return render(request,'404.html',{})
        



    
#def submitUpdate(request):
    
#    if request.method=="POST":
#        form  = Product(request.POST or None)
 #       if form.is_valid():
 #           AddProduct.objects.filter(ProductId = form.ProductId)
#            form.save(
 #           return add(request)
#        else:
 #           for i in form:
 #               print("Errpr ",i.name, i.errors)
 #           print("error in data submission")
#    return render(request,'index.html')
      

    
      
      
      

    
   
    
    
    




        


    

