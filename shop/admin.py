from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from django.db.models.aggregates import Count
from . import models

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
        list_display = ['title', 'products_count']
    list_per_page = 10 

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        return collection.products_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'low'
        return 'ok'

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ["first_name"]
    list_per_page = 10

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']
    ordering = ['id']
    list_per_page = 10
    list_select_related = ['customer']

    

    def customer_first_name(self, order):
        return order.customer.first_name

    def customer_last_name(self, order):
        return order.customer.last_name


# Register your models here.
