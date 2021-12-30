from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from product_app.models import Product, ProductGallary
from product_app.forms import ProductForm
from django.views.generic.list import ListView
from django.views.generic import CreateView

'''
class ProductsView(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'product_temp/products.html'
    context_object_name ='products' 
    paginate_by = 6
'''

def ProductsView(request):
    all = Product.objects.all().order_by('price')
    
    context ={
        'all_products' :all,

        }
    return render(request, 'product_temp/products.html',context)

    
    
def ProductDetailsView(request, slug):
    product_details=Product.objects.get(slug=slug)
    product_gallery=ProductGallary.objects.filter(product=product_details)
    
    context ={
        'product_details' :product_details,
        'product_gallery' :product_gallery,

        }
    return render(request, 'product_temp/product_details.html',context)
 
 

@login_required
def Product_likes(request,slug):
    product = Product.objects.get(slug=slug)

    if request.user in product.likes.all():               # unlike or like depending if the user liked or not
        product.likes.remove(request.user)
        
        return redirect(reverse('product:product_details', args=(slug,)))
    else:
        product.likes.add(request.user)

        return redirect(reverse('product:product_details', args=(slug,))) 
 
 
 
class ProductsCreate(CreateView):
    model = Product
    template_name = 'product_temp/product_create.html'
    #context_object_name ='create_product_form'
    #fields = ('title','short_description','product_cover','content') 
    form_class = ProductForm
    success_url = ''
