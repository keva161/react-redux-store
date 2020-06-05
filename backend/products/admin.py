from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'in_stock', 'trending')
    list_display_links = ('name', 'category')
    list_filter = ('category', 'in_stock', 'trending')
    search_fields = ('products',)
    list_per_page = 25


admin.site.register(Product, ProductAdmin)
