#This code is to let django know that there is a model that needs to be visible to the admin panel
from django.contrib import admin
from .models import *

#Make Django Admin database show the variables inside Display_Fields
#@admin.register(Add_Employee)
#class Add_Employee_Admin(admin.ModelAdmin):
#    list_display = Add_Employee.Display_Fields

admin.site.register(Add_Employee)
