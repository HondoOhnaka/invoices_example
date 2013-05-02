from invoices.signals import invoice_ready
from invoices.models import Invoice

def on_invoice_ready(sender, **kwargs):
    invoice = kwargs['invoice']

    with open('invoice.txt', 'a') as file:
    	file.write("Created an invoice")
    	file.write(invoice.number)

invoice_ready.connect(on_invoice_ready)