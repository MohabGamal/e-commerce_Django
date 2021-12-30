from django.urls import include , path
from product_app import views

app_name='product_app'

urlpatterns = [
    path('', views.ProductsView, name='products'),
    path('create', views.ProductsCreate.as_view(), name='create_products'),
    path('<str:slug>/product_likes/', views.Product_likes, name='product_likes'),
    path('<str:slug>', views.ProductDetailsView, name='product_details'),
    #path('<str:slug>', views.DestinationDetailsView, name='destination_details'),  #must be the last path in the list
                                                                                   #in case i have an url matchs with slug the browser will go to the url not the slug
    

]