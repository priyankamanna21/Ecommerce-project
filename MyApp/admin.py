from re import U
from django.contrib import admin
from MyApp.models import contactQuary,UserDetails,users,order,AddProduct,adminData,CartItem
# Register your models here.
admin.site.register(contactQuary)
admin.site.register(UserDetails)
admin.site.register(users)
admin.site.register(order)
admin.site.register(adminData)
admin.site.register(AddProduct)
admin.site.register(CartItem)

