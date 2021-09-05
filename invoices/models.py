from decimal import Decimal
from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator

import uuid


class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.id}"

    def get_absolute_url(self):
        return reverse("invoice-detail", kwargs={"pk": str(self.id)})

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"


class InvoiceItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice = models.ForeignKey(Invoice, related_name="items", on_delete=models.CASCADE)
    units = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField()
    amount = models.DecimalField(decimal_places=2, max_digits=19, validators=[MinValueValidator(Decimal('0.00'))])

    def __str__(self):
        return f"{self.invoice} - {self.description}"
