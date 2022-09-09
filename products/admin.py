from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price")
    fields = ("title", "image", "price", "external_id", "link")
    search_fields = ("title", "price")
