
from django.db import models
from django.db.models.enums import Choices
from django.utils.text import slugify
from django.contrib.auth.models import User
from martor.models import MartorField

categories = [
    ("Mens_products", "Men's Products"),
    ("Womens_products","Women's Products"),
    ("Accessories", "Accessories"),
    ("Home_products","Home Products"),
          ]

tags = [("New", "New"), ("Sale", "Sale"), ("Discount", "Discount")]

class Product(models.Model) :
    title = models.CharField(max_length=30,)
    author= models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=1)
    published_at= models.DateTimeField(auto_now=True)
    product_cover= models.ImageField(upload_to='media/Products')
    
    price=models.IntegerField(null=False)
    discount=models.IntegerField(blank=True, null=True)
    ratings=models.IntegerField(blank=True, null=True)
    
    short_description = models.TextField(max_length=50)
    likes= models.ManyToManyField(User, blank=True, related_name="likes")
    category = models.CharField(max_length=30, choices=categories, default='Others')
    tag =  models.CharField(max_length=30, choices=tags, null=True, blank=True)
    
    slug= models.SlugField(blank=True, null=True, unique=True)
    content = models.TextField(max_length=500)
    
    
    def save(self,*args, **kwargs):              #overriding save method in admin page
        self.slug= slugify(self.title)           #create a slug
        super(Product,self).save(*args,**kwargs)


    def __str__(self):
         return self.title
    
    
class ProductGallary(models.Model):     # to show destination photos in details # check out admin.py
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'media/Product_gallary')
    

    def __str__(self):
         return '{0}'.format(self.images)