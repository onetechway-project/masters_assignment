from django.contrib import admin

from .models import *


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)


@admin.register(SubCategories)
class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_category_name','category_name')

    def category_name(self, obj):
        if obj.category and obj.category.category_name:
            return obj.category.category_name
        return ''


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'sub_category','category')

    def sub_category(self, obj):
        if obj.sub_category and obj.sub_category.sub_category_name:
            return obj.sub_category.sub_category_name
        return ''

    def category(self, obj):
        if obj.category and obj.category.category_name:
            return obj.obj.category.category_name
        return ''
