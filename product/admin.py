from django.contrib import admin
from .models import Product, Stock, NextDate, Order, Review

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('title', 'author', 'apl_price', 'apl_limit', 'bpl_price', 'bpl_limit', 'aay_price', 'aay_limit', 'is_active')
    search_fields = ['title', 'author']
    list_filter =['is_active',]
    list_editable = ['apl_price', 'apl_limit', 'bpl_price', 'bpl_limit', 'aay_price', 'aay_limit', 'is_active']

admin.site.register(Product, ProductAdmin)

class StockAdmin(admin.ModelAdmin):
    model = Stock
    list_display = ( 'distributor', 'product', 'available', 'is_available')
    search_fields = ['product', 'distributor']
    list_filter =['is_available',]
    list_editable = ['available', 'is_available']
admin.site.register(Stock,StockAdmin)
admin.site.register(NextDate)

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_filter = ['distributor', 'family']
admin.site.register(Order, OrderAdmin)

class ReviewAdmin(admin.ModelAdmin):
    model = Stock
    list_display = ('order', 'title', 'score', 'is_negative')
    list_filter = ['order__distributor', 'is_negative']
    list_editable = ['score', 'is_negative']

admin.site.register(Review, ReviewAdmin)