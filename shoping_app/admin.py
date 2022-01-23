from django.contrib import admin
from .models import Product, Order
# Register your models here.

admin.site.site_header = "Shoping Store"
admin.site.site_title = "Shoping app"
admin.site.index_title = "ABC shoping"

class ProductAdmin(admin.ModelAdmin):
    def category_to_default(self, request, queryset):
        queryset.update(category="default")

    list_display = ('title', 'price', 'discount_price', 'category', 'description')
    search_fields = ('title', 'category')
    actions = ('category_to_default',)
    category_to_default.short_description = "default option for category"
    fields = ('title', "price")
    list_editable = ('description',)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)