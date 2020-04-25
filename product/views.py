from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.views.generic import View,UpdateView
from django.urls import reverse_lazy,reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms,models
from django.contrib.auth.mixins import LoginRequiredMixin
@login_required
def product_create(request):
    registered = False
    if request.method == "POST":
        user_form = forms.ProductForm(data=request.POST)
        if user_form.is_valid():
            use = user_form.save(commit=False)

            #use.save()


            use.save()

            registered = True
            return redirect(reverse_lazy('product'))
        else:
            print(user_form.errors)
    else:

        user_form =forms.ProductForm()
    return render(request,'product_create.html',{
                                    'user_form':user_form,
                                    'registered':registered,
    })


import datetime
class ProductUpdateView(UpdateView,LoginRequiredMixin):
    model = models.Product
    template_name = 'product_update.html'
    form_class = forms.ProductForm
    def form_valid(self, form):
        print(form.instance.date_updated,form.instance.update)
        d=str(datetime.datetime.now())
        d=d.split(" ")
        form.instance.date_updated=d[0]
        form.instance.update=d[1]
        print(form.instance.date_updated,form.instance.update)




        return super().form_valid(form)
