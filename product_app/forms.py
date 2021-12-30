from django import forms
from .models import Product
from martor.fields import MartorFormField


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title','short_description','price','discount','product_cover','content')
        content = MartorFormField()
       

    # categories = forms.ModelMultipleChoiceField(
    #     queryset=Category.objects.all(),            # give many to many field user friendly shape
    #     widget=forms.CheckboxSelectMultiple
    # )

    



