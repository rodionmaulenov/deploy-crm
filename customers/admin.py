from django.contrib import admin

from customers.models import Customer, Tag, Order, Product
admin.site.register(Customer)
admin.site.register(Tag)
admin.site.register(Order)
admin.site.register(Product)
