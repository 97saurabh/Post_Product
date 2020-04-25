from django.urls import path,re_path
from . import views
app_name = 'post'
urlpatterns = [
    path('create/',views.post_create,name='post_create'),
    re_path(r'^(?P<pk>\d+)/update/$',views.PostUpdateView.as_view(),name='post_update'),
    re_path(r'^(?P<pk>\d+)/date/$',views.post_create,name='date_update'),


]
