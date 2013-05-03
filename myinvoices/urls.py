from django.conf.urls import patterns, include, url
from invoices.views import InvoiceListView, InvoiceDetailView, full_invoice

urlpatterns = patterns('',

	url(r'^$', 
	    	InvoiceListView.as_view(
	    		template_name="invoices/invoice_list.html"),
	    	name="invoice_list"),
	url(r'^(?P<pk>\d+)/$',
		InvoiceDetailView.as_view(
			template_name="invoices/invoice_detail.html"),
		name="invoice_detail"),

	url(r'^(?P<pk>\d+)/full/$',
		full_invoice,
		name="full_invoice"),
)