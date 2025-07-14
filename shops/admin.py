from django.contrib import admin
from .models import Shop

class ShopAdmin(admin.ModelAdmin):
    list_display = ('shop_name', 'shop_number', 'category', 'section', 'phone_number')
    search_fields = ('shop_name', 'shop_number', 'category', 'products')

admin.site.register(Shop, ShopAdmin)

