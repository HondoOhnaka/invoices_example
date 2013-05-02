from django.conf.urls import patterns, include, url
from .views import MyInvoiceListView, MyInvoiceDetailView

urlpatterns = patterns('',

	url(r'^$', 
	    	MyInvoiceListView.as_view(
	    		template_name="invoices/invoice_list.html"),
	    	name="invoice_list"),
	url(r'^(?P<pk>\d+)/$',
		MyInvoiceDetailView.as_view(
			template_name="invoices/invoice_detail.html"),
		name="invoice_detail"),
)