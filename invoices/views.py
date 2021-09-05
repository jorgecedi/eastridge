from .models import Invoice, InvoiceItem
from .serializers import InvoiceSerializer, InvoiceItemSerializer
from rest_framework import viewsets


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceItemViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceItemSerializer
    queryset = InvoiceItem.objects.all()

    def get_queryset(self):
        if self.request.query_params.get("invoice"):
            return InvoiceItem.objects.filter(
                invoice=self.request.query_params.get("invoice")
            )
        return InvoiceItem.objects.all()
