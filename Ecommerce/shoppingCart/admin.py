from django.contrib import admin
from shoppingCart.models import Orders,Products,Orders_items
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'image','price','created_At','updated_At')

# class OrdersAdmin(admin.ModelAdmin):
#     list_display = ('id','title', 'description', 'image','price','created_At','updated_At')
admin.site.register(Products,ProductAdmin)
admin.site.register(Orders)
admin.site.register(Orders_items)