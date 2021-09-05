from .models import Invoice, InvoiceItem
from rest_framework import serializers


class InvoiceItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ["url", "id", "invoice", "units", "description", "amount"]


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="invoiceitem-detail",
    )

    class Meta:
        model = Invoice
        fields = ["url", "id", "date", "items"]
