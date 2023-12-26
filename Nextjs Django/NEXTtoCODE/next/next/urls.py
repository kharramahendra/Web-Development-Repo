"""next URL Configuration

The `urlpatterns` list routes URLs to user. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function user
    1. Add an import:  from my_app import user
    2. Add a URL to urlpatterns:  path('', user.home, name='home')
Class-based user
    1. Add an import:  from other_app.user import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from API import user
from API import products
from API import transaction
from API import myorders

urlpatterns = [
    path('admin/', admin.site.urls),

    #-----USER APIs-----
    path('signup/',user.signup),
    path('login/',user.login),
    path('getuser/',user.getuser),
    path('updateuser/',user.updateuser),
    path('updatepassword/',user.updatepassword),

    #-----PRODUCTS APIs-------
    path('getproducts/',products.getproducts),
    path('getproduct/',products.getproduct),


    #-----TRANSACTION APIs----
    path('pretransaction/',transaction.pretransaction),
    path('posttransaction/',transaction.posttransaction),


    #-----ORDER AND PINCODE APIs-----------
    path('myorders/',myorders.myorders),
    path('order/',myorders.order)


]
