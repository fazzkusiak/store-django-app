from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from tags.models import TaggedItem
from shop.admin import ProductAdmin
from shop.models import Product

# Create your models here.
class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem

class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]

admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)