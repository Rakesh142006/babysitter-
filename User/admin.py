from django.contrib import admin
from .models import *
# Register your models here.

class cust_(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile','address','reg_date']

admin.site.register(Customer,cust_)

class con_(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile','message']

admin.site.register(Contact,con_)


class sc_(admin.ModelAdmin):
    list_display = ['type', 'image']

admin.site.register(Sitters_category,sc_)