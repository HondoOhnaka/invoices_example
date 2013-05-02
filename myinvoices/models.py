from django.db import models
from django.contrib.auth.models import User
from invoices import Invoice

class MyInvoice(Invoice):
	invoice_for = models.ForeignKey(User, related_name="for_users")
	class Meta:
		verbose_name=u'My Invoice'