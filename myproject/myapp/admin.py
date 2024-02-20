from django.contrib import admin

# Register your models here.
from .models import User, Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price", "digits"]
    ordering = ["name"]
    list_filter = ["date_product_added"]
    search_fields = ["name"]
    search_help_text = "Поиск по названию продукта"
    readonly_fields = ["date_product_added"]
    fieldsets = [
        (
            None,
                {
                    'fields': ['name'],
                },
        ),
        (
            'Подробности',
                {
                    'classes': ['collapse', 'wide'],
                    'description': 'Подробное описание товара',
                    'fields': ['description'],
                },
        ),
        (
            None,
                {
                    'fields': ['price', 'digits'],
                }
        )
]


class UserAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_filter = ["date_created"]
    search_fields = ["name"]
    search_help_text = "Поиск по имени пользователя"
    readonly_fields = ["date_created"]

class OrderAdmin(admin.ModelAdmin):
    ordering = ["date_ordered"]
    list_filter = ["date_ordered"]
    search_fields = ["date_ordered"]
    search_help_text = "Поиск по дате заказа"
    readonly_fields = ["date_ordered"]

admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

