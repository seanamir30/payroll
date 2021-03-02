#This code is to let django know that there is a model that needs to be visible to the admin panel
from django.contrib import admin
from .models import *

class Add_Employee_Admin(admin.ModelAdmin):
	ordering = ('id',)
	list_display = ('id','name','position','email')
	readonly_fields = ('id',)

admin.site.register(Add_Employee, Add_Employee_Admin)
