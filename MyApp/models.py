
from itertools import product
from statistics import quantiles
from django.db import models

# Create your models here
class users(models.Model):
    Name=models.TextField()
    Email=models.EmailField(primary_key=True)
    Password=models.TextField()
    Phone=models.CharField(max_length=10,null=True,blank=True)
    class Meta:
        db_table='users'
        
class AddProduct(models.Model):
    ProductId=models.IntegerField(primary_key=True)
    ProductName=models.CharField(max_length=2000)
    Quantity=models.IntegerField()
    CostPrice=models.IntegerField()
    SalePrice=models.IntegerField()
    Pimage=models.ImageField(upload_to='img/products',default="")
    
    def _str_(self):
        return self.name + ": " + str(self.Pimage)
    class Meta:
         db_table='AddProduct'
         

class ProductDescip(models.Model):
    Product=models.ForeignKey(AddProduct,on_delete=models.CASCADE)
    description=models.CharField(max_length=255,null=True,blank=True)
    
    class Meta:
        db_table='ProductDescrip'

class order(models.Model):
    orderNo=models.IntegerField(primary_key=True)
    userId=models.ForeignKey(users,on_delete=models.SET_NULL,null=True)
    dateOfOrder=models.DateTimeField(auto_now=True)
    Product=models.ForeignKey(AddProduct,on_delete=models.SET_NULL,null=True)
    Quantity=models.IntegerField()
    TotalAmt=models.IntegerField()
    CompleteTrans=models.BooleanField()
    class Meta:
        db_table='order'
        
class UserDetails(models.Model):
    
    Email=models.ForeignKey(users,on_delete=models.SET_NULL,null=True)
    Phone=models.CharField(primary_key=True,max_length=10)
    Address=models.TextField()
    orderNo=models.ForeignKey(order,on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table='UserDetails'
class contactQuary(models.Model):
    Name=models.TextField()
    Email=models.EmailField()
    Phone=models.CharField(primary_key=True,max_length=10)
    Subject=models.TextField()
    Message=models.TextField()
    
    class Meta:
        db_table='contactQuary'

class adminData(models.Model):
    Username=models.TextField()
    Email=models.EmailField(primary_key=True)
    Password=models.TextField()
    class Meta:
        db_table='admin'  

class CartItem(models.Model):
    CartId=models.AutoField(primary_key=True)
    product=models.ForeignKey(AddProduct,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    date_added=models.DateTimeField(auto_now=True)
    class Meta:
        db_table='CartItem'

    


    
    
         
        

    