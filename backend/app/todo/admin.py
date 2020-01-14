from django.contrib import admin
from .models import Todo, Branch, Customer

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

class BranchAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'location')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone_number', 'email', 'address')

    # Register your models here.
admin.site.register(Todo, TodoAdmin) #make sure no tabs for line

admin.site.register(Branch, BranchAdmin)

admin.site.register(Customer, CustomerAdmin)