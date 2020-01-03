from django.contrib import admin
from .models import Todo, Branch

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

    # Register your models here.
admin.site.register(Todo, TodoAdmin) #make sure no tabs for line

admin.site.register(Branch)