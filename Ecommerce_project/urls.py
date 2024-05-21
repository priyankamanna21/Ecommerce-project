"""
Ecommerce_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path
from MyApp import views as v
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Uncomment the next line to enable the admin:
    #path('admin/', admin.site.urls),
    path('',v.ind1,name=''),
    path('home',v.home),
    path('logout',v.logout1,name='logout'),
   # path('register',v.register,name='register'),
    path('index2',v.ind2,name='index2'),
    path('login',v.login,name='login'),
    path('registration',v.registration,name='register'),
    path('shopping',v.sho,name='shopping'),
    path('abo',v.abt, name='abo'),
    path('ca',v.cart,name='ca'),
    path('vie',v.view,name='vie'),
    path('check',v.cheout,name='check'),
    path('sinproduct',v.sproduct,name='sinproduct'),
    path('sinnew',v.snews,name='sinnew'),
    path('404',v.file404,name='404'),
    path('contc',v.submitQuary,name='contc'),
    path('new',v.news,name='new'),
    path('addproduct',v.add,name='add'),
    path('deleteItem/<int:pk>',v.DeleteData,name='delete_items'),
    path('updateprod',v.updatedata),
    path('delprod/<int:pk>',v.delprod,name='deleteprod'),
    path('update/<int:pk>',v.updatedata,name='update_items'),
    path('search',v.search,name='search_products'),
    #path('mail',v.mail,name='send_mail'),
    path('details/<int:pk>',v.detail,name='details'),
    #path('submit',v.submitUpdate,name='submitupdate'),

    path('decrease_quantity/<int:product_id>/', v.decrease_quantity, name='decrease_quantity'),
    path('increase_quantity/<int:product_id>/', v.increase_quantity, name='increase_quantity'),


   # path('showproduct',v.show_product),
   path('add_to_cart/<int:product_id>',v.add_to_cart,name="add_to_cart"),
   #path('checkout',v.checkout1,name="checking"),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)