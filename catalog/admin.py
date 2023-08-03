from django.contrib import admin

from catalog.models import Category, Product, Version


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'specification',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_title', 'version_number', 'sign_current_version',)
    list_filter = ('version_title',)
