from django.contrib import admin
from .models import Computers
# Register your models here.
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('id','comp_name','date_of_created')
    search_fields = ['comp_name','id']
admin.site.register(Computers,ComputerAdmin)