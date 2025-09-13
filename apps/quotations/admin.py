from django.contrib import admin
from .models import QuotationRequest

@admin.register(QuotationRequest)
class QuotationRequestAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ("id", "name", "email", "contact", "country", "category", "product", "quantity", "created_at")

    # Fields to enable searching
    search_fields = ("name", "email", "contact", "product", "category", "country")

    # Add filters for quick navigation
    list_filter = ("category", "country", "created_at")

    # Order records by latest created first
    ordering = ("-created_at",)

    # Make these fields read-only in the admin form (optional)
    readonly_fields = ("created_at",)
