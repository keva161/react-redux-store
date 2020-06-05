from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    list_per_page = 25


admin.site.register(Category, CategoryAdmin)
