from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from post.models import Post
from product.models import Product
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'




def home(request):
    data=Post.objects.all()
    return render(request,'index.html',{'data':data,})

def product(request):
    data=Product.objects.all()
    return render(request,'product.html',{'data':data,})
