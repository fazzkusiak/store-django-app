from typing import Any
from django.contrib import admin, messages
from django.http import HttpRequest
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'products_count']
    list_per_page = 10 

    
    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
            reverse('admin:shop_product_changelist') 
            + '?'
            + urlencode({
                'collection__id': str(collection.id)

        })
        )
        return format_html('<a href={}>{}</a>', url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )
   

class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [ 
            ('<10', 'Low')
        ]

    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lte=10)

    

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    prepopulated_fields = {
        'slug': ['title']
    }
    actions = ['clear_inventory']
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    list_filter = ['collection', 'last_update', InventoryFilter]

   
    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'low'
        return 'ok'

    @admin.display(description="Clear inventory")
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(request, f"{updated_count} were succesfully updated", messages.SUCCESS )
        
        


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders']
    list_editable = ['membership']
    list_per_page = 10
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    @admin.display(ordering='orders')
    def orders(self, customer):
        # ?customer_id=1
        url = (
            reverse('admin:shop_order_changelist')
            + '?' 
            + urlencode({
                'customer__id': str(customer.id)
            })
            )
        
        return format_html('<a href={}>{}</a>', url, customer.orders)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders = Count('order')
        )

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    list_display = ['id', 'placed_at', 'customer']
    ordering = ['id']
    list_per_page = 10
    list_select_related = ['customer']
        


# Register your models here.
