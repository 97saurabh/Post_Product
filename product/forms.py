from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    #meta class is used to directly take entry of a form to given models
    class Meta():
        model=Product
        fields=('title','weight','des','price',)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].label = 'Product Title'
        self.fields['des'].label = "About Product"
        self.fields['weight'].label = 'Weight in Kg'
        self.fields['price'].label = "Rupees"
