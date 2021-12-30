from django.contrib import admin
from .models import Product, ProductGallary


#admin.site.register(Product)


class ProductGallaryAdmin(admin.StackedInline):
    model = ProductGallary

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductGallaryAdmin]         # to inline two models as one and give ability to upload more than one file
 
    class Meta:
       model = Product