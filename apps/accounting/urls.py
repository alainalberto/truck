from django.conf.urls import *
from django.contrib.auth.decorators import login_required, permission_required
from apps.accounting.views import *
from django.views.generic.dates import ArchiveIndexView
from apps.accounting.components.AccountingPDF import Receipt_pdf, Invoices_pdf

urlpatterns = [
    url(r'^accounts/statistic/$', login_required(AccountingPanel), name='panel_account'),

    #Account
    url(r'^accounts/$', login_required(permission_required('accounting.add_account')(AccountsViews)), name='accounts'),
    url(r'^accounts/create/$', login_required(permission_required('accounting.account.add_account')(AccountCreate.as_view())), name='account_create'),
    url(r'^accounts/description/(?P<pk>\d+)/$', login_required(permission_required('accounting.add_accountdescrip')(AccountsDescViews)), name='account_descrip'),
    url(r'^accounts/description/$', login_required(permission_required('accounting.add_accountdescrip')(AccountsDescAllViews)), name='account_descripall'),
    url(r'^accounts/document/(?P<pk>\d+)/$', login_required(permission_required('accounting')(AccountDocument)), name='account_document'),

    #Customers
    url(r'^customers/$', login_required(permission_required('accounting.add_customer')(CustomersView.as_view())), name='customers'),
    url(r'^customers/create$', login_required(permission_required('accounting.add_customer')(CustomersCreate.as_view())), name='customer_create'),
    url(r'^customers/edit/(?P<pk>\d+)/$', login_required(permission_required('accounting.change_customer')(CustomersEdit.as_view())), name='customer_edit'),
    url(r'^customers/(?P<pk>\d+)/$', login_required(permission_required('accounting.delete_customer')(CustomersDelete.as_view())), name='customer_delete'),
    url(r'^customers/view/(?P<pk>\d+)/$', login_required(permission_required('accounting.change_customer')(CustomerView)), name='customer_view'),
    url(r'^customers/create/(?P<popup>[^/]+)/$', login_required(permission_required('accounting.add_customer')(CustomersCreate.as_view())), name='customer_popup'),

   #Receipts
    url(r'^receipts/$', login_required(permission_required('accounting.add_receipt')(ReceiptsView.as_view())), name='receipts'),
    url(r'^receipts/create$', login_required(permission_required('accounting.add_receipt')(ReceiptsCreate.as_view())), name='receipts_create'),
    url(r'^receipts/edit/(?P<pk>\d+)/$', login_required(permission_required('accounting.change_receipt')(ReceiptsEdit.as_view())), name='receipts_edit'),
    url(r'^receipts/(?P<pk>\d+)/$', login_required(permission_required('accounting.delete_receipt')(ReceiptsDelete.as_view())), name='receipts_delete'),
    url(r'^receipts/print/(?P<pk>\d+)/$', login_required(permission_required('accounting.add_receipt')(Receipt_pdf)), name='receipts_pdf'),


    #Payments
    url(r'^payments/$', login_required(permission_required('accounting.add_payment')(PaymentView.as_view())), name='payments'),
    url(r'^payments/create$', login_required(permission_required('accounting.add_payment')(PaymentCreate.as_view())), name='payments_create'),
    url(r'^payments/edit/(?P<pk>\d+)/$',login_required(permission_required('accounting.change_payment')(PaymentEdit.as_view())), name='payment_edit'),
    url(r'^payments/(?P<pk>\d+)/$',login_required(permission_required('accounting.delete_payment')(PaymentDelete.as_view())),  name='payment_delete'),


    #Employees
    url(r'^employees/$', login_required(permission_required('accounting.add_employee')(EmployeesView.as_view())), name='employees'),
    url(r'^employees/create$', login_required(permission_required('accounting.add_employee')(EmployeesCreate.as_view())), name='employees_create'),
    url(r'^employees/edit/(?P<pk>\d+)/$', login_required(permission_required('accounting.change_employee')(EmployeesEdit.as_view())), name='employees_edit'),
    url(r'^employees/(?P<pk>\d+)/$', login_required(permission_required('accounting.delete_employee')(EmployeesDelete.as_view())), name='employees_delete'),

    #Invoices
    url(r'^invoices/$', login_required(permission_required('accounting.add_invoice')(ArchiveIndexView.as_view(model=Invoice, date_field="start_date", template_name = 'accounting/invoices/invoicesViews.html'))), name='invoices'),
    url(r'^invoices/create$', login_required(permission_required('accounting.add_invoice')(InvoicesCreate)), name='invoices_create'),
    url(r'^invoices/edit/(?P<pk>\d+)/$', login_required(permission_required('accounting.change_invoice')(InvoicesEdit.as_view())), name='invoices_edit'),
    url(r'^invoices/(?P<pk>\d+)/$', login_required(permission_required('accounting.delete_invoice')(InvoicesDelete.as_view())), name='invoices_delete'),
    url(r'^invoices/print/(?P<pk>\d+)/$', login_required(permission_required('accounting.add_invoice')(Invoices_pdf)), name='invoices_pdf'),
    url(r'^invoices/view/(?P<pk>\d+)/$', login_required(permission_required('accounting.add_invoice')(InvoiceView)), name='invoices_view'),

    #Customer Note
    url(r'^customer/note/create/(?P<pk>\d+)/$', login_required(permission_required('accounting.add_note')(NoteCreate.as_view())), name='note_create'),
    url(r'^customer/note/edit/(?P<pk>\d+)/$', login_required(permission_required('accounting.change_note')(NoteEdit.as_view())), name='note_edit'),
    url(r'^customer/note/(?P<pk>\d+)/$', login_required(permission_required('accounting.delete_note')(NoteDelete.as_view())), name='note_delete'),

]