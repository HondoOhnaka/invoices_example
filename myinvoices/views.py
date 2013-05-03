from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from invoices.views import InvoiceListView, InvoiceDetailView
from .models import MyInvoice

class MyInvoiceListView(InvoiceListView):
	model = MyInvoice
	context_object_name = 'invoice_list'
	def get_queryset(self):
		return MyInvoice.objects.all()

class MyInvoiceDetailView(InvoiceDetailView):
	model = MyInvoice
	context_object_name = 'invoice'

	def get_object(self):
		invoice = get_object_or_404(MyInvoice, pk=self.kwargs['pk'])
		return invoice

def full_invoice(request, pk):
	invoice = get_object_or_404(MyInvoice, pk=pk)
	items = invoice.items.all

	ctx = RequestContext(request, {
		'invoice': invoice,
		'items': items,
		})
	return render_to_response('invoices/full_invoice.html', ctx)
