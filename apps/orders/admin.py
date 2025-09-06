from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ("product", "quantity", "price")
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "full_name", "email", "phone", "total_amount", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("user__email", "full_name", "email", "phone")
    readonly_fields = ("created_at",)
    inlines = [OrderItemInline]
