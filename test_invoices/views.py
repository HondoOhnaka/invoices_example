from invoices.models import Invoice
from invoices.views import InvoiceListView

class MyInvoiceListView(InvoiceListView):
    def get_queryset(self):
        return Invoice.objects.all()