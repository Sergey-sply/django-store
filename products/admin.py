from django.contrib import admin

from products.models import Categories, Products

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name',]

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'quantity', 'price', 'discout']
    list_editable = ['discout',]
    search_fields = ['name', 'discription']
    list_filter = ['discout', 'quantity', 'category']
    fields = [
        'name',
        'category',
        'slug',
        'description',
        'image',
        ('price', 'discout'),
        'quantity',
    ]