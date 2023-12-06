from django.contrib import admin

# Register your models here.
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    #prepopulated_fields = {'slag': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'created', 'uploaded']
    list_filter = ['available', 'created', 'uploaded']
    #list_editable = ['price', 'available']
    #prepopulated_fields = {'slag': ('name',)}
