from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from invoices.models import Invoice, InvoiceItem


class InvoiceTestCase(TestCase):
    baseURL = "http://testserver"

    def test_api_create_invoice(self):
        client = APIClient()
        response = client.post(
            "/api/v1/invoices/",
            {
                "date": "2021-09-05T17:39:33.593620+00:00",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_read_invoices(self):
        for i in range(10):
            invoice_date = "2021-09-05T17:39:33.593620+00:00"
            Invoice.objects.create(date=invoice_date)

        client = APIClient()
        response = client.get("/api/v1/invoices/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 10)

    def test_api_read_invoice(self):
        invoice_date = "2021-09-05T17:39:33.593620+00:00"
        invoice = Invoice.objects.create(date=invoice_date)

        client = APIClient()
        response = client.get(f"/api/v1/invoices/{invoice.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["id"], str(invoice.id))

    def test_api_create_invoice_item(self):
        invoice_date = "2021-09-05T17:39:33.593620+00:00"
        invoice = Invoice.objects.create(date=invoice_date)
        invoice_url = f"{self.baseURL}{invoice.get_absolute_url()}"

        client = APIClient()
        response = client.post(
            "/api/v1/invoice-items/",
            {
                "invoice": invoice_url,
                "units": 10,
                "description": "Short test description",
                "amount": 15.0,
            },
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["invoice"], invoice_url)

    def test_api_read_invoice_items(self):
        invoice_date = "2021-09-05T17:39:33.593620+00:00"
        invoice = Invoice.objects.create(date=invoice_date)
        for i in range(10):
            InvoiceItem.objects.create(
                invoice=invoice,
                units=10,
                description="Short test description",
                amount=15.0,
            )

        client = APIClient()
        response = client.get("/api/v1/invoice-items/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 10)

    def test_api_read_invoice_item(self):
        invoice_date = "2021-09-05T17:39:33.593620+00:00"
        invoice = Invoice.objects.create(date=invoice_date)
        invoice_url = f"{self.baseURL}{invoice.get_absolute_url()}"

        invoice_item = InvoiceItem.objects.create(
            invoice=invoice, units=10, description="Short description", amount=15.0
        )

        client = APIClient()
        response = client.get(f"/api/v1/invoice-items/{invoice_item.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["invoice"], invoice_url)

    def test_api_filter_invoice_items_by_invoice(self):
        invoice_date = "2021-09-05T17:39:33.593620+00:00"
        invoice = Invoice.objects.create(date=invoice_date)
        for i in range(5):
            InvoiceItem.objects.create(
                invoice=invoice,
                units=10,
                description="Short test description",
                amount=15.0,
            )
        for i in range(5):
            InvoiceItem.objects.create(
                invoice=Invoice.objects.create(date=invoice_date),
                units=10,
                description="Short test description",
                amount=15.0,
            )

        client = APIClient()
        response = client.get(f"/api/v1/invoice-items/?invoice={invoice.id}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 5)
