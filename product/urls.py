from django.urls import path,re_path
from . import views
app_name = 'product'
urlpatterns = [
    path('create/',views.product_create,name='product_create'),
    re_path(r'^(?P<pk>\d+)/update/$',views.ProductUpdateView.as_view(),name='product_update'),



]
