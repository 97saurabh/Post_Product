from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy,reverse
# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=25,blank=False)
    weight=models.IntegerField()
    price=models.IntegerField()
    des=models.TextField(max_length=1000)
    date_created = models.DateField(auto_now_add=True)
    create = models.TimeField(auto_now_add=True)
    date_updated = models.DateField(null=True,blank=True)
    update = models.TimeField(null=True,blank=True)
    def get_absolute_url(self):
        return reverse('home')
    def __str__(self):
        return self.title
