from django.contrib import admin
from .models import *

class categoryadmin(admin.ModelAdmin):
    list_display = ('name','image','description') 
class productadmin(admin.ModelAdmin):
    list_display = ('Name','original_price','Description')  
    
admin.site.register(Category,categoryadmin)
admin.site.register(Products)