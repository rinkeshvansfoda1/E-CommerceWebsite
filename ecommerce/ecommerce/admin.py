from django.contrib import admin
from .models import Product, Product_jeans, Product_laptop, Product_phone, Product_smarttv, Product_washing_machine 

# Register your models here

admin.site.register(Product)
admin.site.register(Product_laptop)
admin.site.register(Product_washing_machine)
admin.site.register(Product_phone)
admin.site.register(Product_smarttv)
admin.site.register(Product_jeans)