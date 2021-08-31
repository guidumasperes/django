from django.contrib import admin

# Register your models here.
from .models import Pet

@admin.register(Pet) #we need to register this class with admin to tell which model it's associated with
class PetAdmin(admin.ModelAdmin):
    #list_display allows us to to define which fields are displayed on this listing screen
    list_display = ['name', 'species', 'breed', 'age', 'sex']
