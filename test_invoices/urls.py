from django.conf.urls import patterns, include, url
from invoices.views import InvoiceDetailView
from .views import MyInvoiceListView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^invoices/$', 
    	MyInvoiceListView.as_view(),
    	name="invoice_list"),
    url(r'^invoice/(?P<pk>\d+)/$',
    	InvoiceDetailView.as_view(),
    	name="invoice_detail"),
)
