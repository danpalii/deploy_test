from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'quantity', 'price', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)