from django.db import models

class QuotationRequest(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    product = models.JSONField(default=list)   # store list of products
    quantity = models.JSONField(default=list)  # store list of quantities
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.product}"
