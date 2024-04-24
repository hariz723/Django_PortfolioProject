from django.db import models
from django.contrib.auth.models import User
import datetime 
import os

def Getfilename(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%H:%S")
    new_filename = "%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Category(models.Model):
    name=models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=Getfilename,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    create_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.name

class Products(models.Model):
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=150, null=False, blank=False)
    vendor=models.CharField(max_length=150, null=False, blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    product_price=models.FloatField(null=False,blank=False)
    product_image = models.ImageField(upload_to=Getfilename,null=True,blank=True)
    Description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
    create_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.name 

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Products=models.ForeignKey(Products,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    create_at=models.DateTimeField(auto_now_add=True)
       