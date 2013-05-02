from invoices.views import InvoiceListView, InvoiceDetailView
from .models import MyInvoice

class MyInvoiceListView(InvoiceListView):
	model = MyInvoice
	context_object_name = 'invoice_list'
	def get_queryset(self):
		return MyInvoice.objects.all()

class MyInvoiceDetailView(InvoiceDetailView):
	model = MyInvoice
