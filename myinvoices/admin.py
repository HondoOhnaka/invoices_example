from django.contrib import admin
from django import forms
from django.utils.translation import ugettext, ungettext, ugettext_lazy as _

from .models import MyInvoice
from invoices.models import Item, LineItem, LineItemType, LineItemGroup
from invoices import cancel_invoice

class MyInvoiceForm(forms.ModelForm):
    class Meta:
        model = MyInvoice
        fields = ('invoice_for', 'user', 'begins', 'ends', 'is_paid')

class MyInvoiceAdmin(admin.ModelAdmin):
    form = MyInvoiceForm
    readonly_fields = ('total_amount',)
    list_display = ('invoice_for', 'user', 'begins', 'ends', 'total_amount', 'is_paid')
    list_filter = ('is_paid',)
    actions = ['cancel_invoices']

    def cancel_invoices(self, request, queryset):

        for invoice in queryset:
            cancel_invoice(invoice)

        message = ungettext("successfully cancelled %(count)d invoice",
            "successfully cancelled %(count)d invoices", queryset.count()) % {'count': queryset.count()}
        self.message_user(request, message)
    cancel_invoices.short_description = _('Cancel selected invoices')

# class ItemAdmin(admin.ModelAdmin):
#     pass
# class LineItemAdmin(admin.ModelAdmin):
#     pass
# class LineItemGroupAdmin(admin.ModelAdmin):
#     pass
# class LineItemTypeAdmin(admin.ModelAdmin):
#     pass

admin.site.register(MyInvoice, MyInvoiceAdmin)
# admin.site.register(Item, ItemAdmin)
# admin.site.register(LineItem, LineItemAdmin)
# admin.site.register(LineItemGroup, LineItemGroupAdmin)
# admin.site.register(LineItemType, LineItemTypeAdmin)


