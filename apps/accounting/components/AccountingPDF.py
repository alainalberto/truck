from io import BytesIO
import time
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.platypus import Paragraph, Table, TableStyle
from apps.logistic.models import Load, DispatchHasPayment, DriversHasPayment, LoadsHasFee, InvoicesHasLoad, DriversLogt, DispatchLogt, Diesel, PaymentHasLoad
from apps.accounting.models import *
from apps.logistic.models import Load, InvoicesHasLoad, DriversLogt


def Receipt_pdf(request, pk):
    recpt = Receipt.objects.get(id_rec = pk)
    response = HttpResponse(content_type='application/pdf')
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    #Header
    p.setFillColor('#2471A3')
    p.roundRect(0, 750, 694, 120, 20, fill=1)
    p.drawImage('static/img/logoFCI.png', 250, 760, width=150, height=70)

    p.setFont('Helvetica', 28)
    p.setFillColor('#34495E')
    p.drawCentredString(70, 700, "RECEIPT")


    p.setFont('Helvetica-Bold', 12)
    p.drawString(50, 680, 'No. '+str(recpt.serial))

    p.setFont('Helvetica',12)
    p.setFillColorRGB(0,0,0)
    p.drawString(460, 700, 'Date: '+str(recpt.start_date))
    p.line(450, 697, 562, 697)

    #Footer
    p.setFont('Helvetica', 9)
    p.setFillColorRGB(0, 0, 0)
    p.line(0, 50, 800, 50)
    p.drawString(30, 20, 'Date of printing '+time.strftime("%m/%d/%y %H:%M:%S")+' by %s' % request.user.first_name)

    #Boby
    styles = getSampleStyleSheet()
    stylesBH = styles["Heading3"]
    stylesBH.alignment = TA_CENTER
    stylesBH.fontSize = 10
    stylesBH.fill = '#34495E'
    description = Paragraph('''Description''',stylesBH)
    waytopay = Paragraph('''Payment Method''',stylesBH)
    value = Paragraph('''Total''',stylesBH)
    data = []
    data.append([description, waytopay, value])

    stylesBD = styles["BodyText"]
    stylesBD.alignment = TA_CENTER
    stylesBD.fontSize = 7
    high = 550
    this_receipt = [recpt.description, recpt.waytopay, recpt.total]
    data.append(this_receipt)
    high = high - 18

    width, height = A4
    table = Table(data, colWidths=[11 * cm, 4 * cm, 2 * cm])
    table.setStyle(TableStyle([
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ]))
    table.wrapOn(p, width, height)
    table.drawOn(p, 40, high)

    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def Invoices_pdf(request, pk):
    invoice = Invoice.objects.get(id_inv = pk)
    customer = Customer.objects.get(id_cut=invoice.customers_id)
    descrip = InvoicesHasItem.objects.filter(invoices=invoice)
    business = Busines.objects.get(id_bus=invoice.business_id)
    response = HttpResponse(content_type='application/pdf')
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    #Header
    p.setFillColor('#2471A3')
    p.roundRect(0, 750, 694, 120, 20, fill=1)
    p.drawImage('static/img/logoFCI.png', 250, 760, width=150, height=70)

    p.setFont('Helvetica', 28)
    p.setFillColor('#E5E7E9')
    p.drawCentredString(70, 785, "INVOICE")

    p.setFillColor('#34495E')
    p.setFont('Helvetica-Bold', 12)
    p.drawString(50, 730, 'No. '+invoice.prefix+"-"+str(invoice.serial))

    p.setFont('Helvetica', 10)
    p.drawImage('static/img/icon/address-o.png', 50, 700, width=10, height=10)
    p.drawString(65, 700, business.address)
    p.drawImage('static/img/icon/phone-o.png', 50, 680, width=10, height=10)
    p.drawString(65, 680, business.phone)
    if business.fax:
      p.drawImage('static/img/icon/fax-o.png', 50, 660, width=10, height=10)
      p.drawString(65, 660, business.fax)


    p.setFont('Helvetica',12)
    p.setFillColorRGB(0,0,0)
    p.drawString(460, 700, 'Date: '+str(invoice.start_date))
    p.line(450, 697, 562, 697)

    #Customer
    if customer.company_name:
        p.setFillColor('#34495E')
        p.setFont('Helvetica-Bold', 14)
        p.drawString(75, 620, customer.company_name)
        p.drawString(50, 620, 'To:')
    if customer.fullname:
        p.setFont('Helvetica-Bold', 12)
        p.drawString(75, 600, customer.fullname)
    if customer.address:
        p.setFont('Helvetica', 12)
        p.drawString(75, 580, customer.address)
    if customer.phone:
        p.setFont('Helvetica', 12)
        p.drawString(75, 560, customer.phone)


    #Footer
    p.setFillColor('#2471A3')
    p.roundRect(0, 0, 694, 50, 0, fill=1)
    p.setFont('Helvetica', 9)
    p.setFillColorRGB(0, 0, 0)
    p.line(0, 50, 800, 50)
    user_print = ""
    if request.user.first_name:
        user_print = request.user.first_name+" "+request.user.last_name
    else:
        user_print= request.user.username
    p.drawString(30, 20, 'Date of printing '+time.strftime("%m/%d/%y %H:%M:%S")+' by %s' % user_print)
    p.setFillColor('#34495E')
    p.setFont('Helvetica', 10)
    p.drawString(200, 60, 'THANK YOU FOR YOUR BUSSINESS!')


    #Boby
    p.setFillColor('#020000')
    p.setFont('Helvetica-Bold', 14)
    p.drawString(450, 590, "Total: $"+ str(invoice.total))
    p.setFont('Helvetica', 12)
    p.drawString(450, 570, "Discount: $" + str(invoice.discount))
    p.setFont('Helvetica', 12)
    p.drawString(450, 550, "Subtotal: $" + str(invoice.subtotal))

    styles = getSampleStyleSheet()
    stylesBH = styles["Heading3"]
    stylesBH.alignment = TA_CENTER
    stylesBH.fontSize = 10
    stylesBH.fill = '#34495E'
    quantity = Paragraph('''Quantity''', stylesBH)
    description = Paragraph('''Description''', stylesBH)
    value = Paragraph('''Unit Price''',stylesBH)
    tax = Paragraph('''Tax %''', stylesBH)
    subtotal = Paragraph('''Subtotal''', stylesBH)
    data = []
    data.append([quantity, description, value, tax, subtotal])

    stylesBD = styles["BodyText"]
    stylesBD.alignment = TA_CENTER
    stylesBD.fontSize = 7
    high = 510
    for item in descrip:
        this_descrip = [item.quantity, item.description, item.value, item.tax, item.subtotal]
        data.append(this_descrip)
        high = high - 18

    width, height = A4
    table = Table(data, colWidths=[2 * cm, 8 * cm, 4 * cm, 2 * cm])
    table.setStyle(TableStyle([
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ]))
    table.wrapOn(p, width, height)
    table.drawOn(p, 40, high)

    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def InvoicesLod_pdf(request, pk):
    invoice = Invoice.objects.get(id_inv = pk)
    customer = Customer.objects.get(id_cut=invoice.customers_id)
    descrip = []
    loadInv = InvoicesHasLoad.objects.filter(invoices_id=invoice.id_inv)
    for l in loadInv:
        load = Load.objects.get(id_lod=l.loads_id)
        descrip.append(load)
    business = Busines.objects.get(id_bus=invoice.business_id)
    response = HttpResponse(content_type='application/pdf')
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    #Header
    p.setFillColor('#2471A3')
    p.roundRect(0, 750, 694, 120, 20, fill=1)
    p.drawImage('static/img/truck.jpg', 440, 760, width=150, height=70)

    p.setFont('Helvetica', 16)
    p.setFillColor('#E5E7E9')
    p.drawCentredString(300, 785, business.name)
    if business.messager:
      p.setFont('Helvetica', 12)
      p.setFillColor('#E5E7E9')
      p.drawCentredString(300, 740, business.messager)

    p.setFont('Helvetica', 28)
    p.setFillColor('#E5E7E9')
    p.drawCentredString(70, 785, "INVOICE")

    p.setFillColor('#34495E')
    p.setFont('Helvetica-Bold', 12)
    p.drawString(410, 720, 'No: '+invoice.prefix+"-"+str(invoice.serial))

    p.setFont('Helvetica', 10)
    p.drawImage('static/img/icon/address-o.png', 50, 700, width=10, height=10)
    p.drawString(65, 700, business.address)
    p.drawImage('static/img/icon/phone-o.png', 50, 680, width=10, height=10)
    p.drawString(65, 680, business.phone)
    if business.fax:
      p.drawImage('static/img/icon/fax-o.png', 50, 660, width=10, height=10)
      p.drawString(65, 660, business.fax)


    p.setFont('Helvetica',11)
    p.setFillColorRGB(0,0,0)
    p.drawString(410, 700, 'Week Star Date: '+str(invoice.start_date))
    p.drawString(410, 680, 'Week End Date: ' + str(invoice.end_date))


    #Customer
    '''if customer.company_name:
        p.setFillColor('#34495E')
        p.setFont('Helvetica-Bold', 14)
        p.drawString(75, 620, customer.company_name)
        p.drawString(50, 620, 'To:')
    if customer.fullname:
        p.setFont('Helvetica-Bold', 12)
        p.drawString(75, 600, customer.fullname)
    if customer.address:
        p.setFont('Helvetica', 12)
        p.drawString(75, 580, customer.address)
    if customer.phone:
        p.setFont('Helvetica', 12)
        p.drawString(75, 560, customer.phone)


    #Footer
    p.setFillColor('#2471A3')
    p.roundRect(0, 0, 694, 50, 0, fill=1)
    p.setFont('Helvetica', 9)
    p.setFillColorRGB(0, 0, 0)
    p.line(0, 50, 800, 50)
    user_print = ""
    if request.user.first_name:
        user_print = request.user.first_name+" "+request.user.last_name
    else:
        user_print= request.user.username
    p.drawString(30, 20, 'Date of printing '+time.strftime("%m/%d/%y %H:%M:%S")+' by %s' % user_print)
    p.setFillColor('#34495E')
    p.setFont('Helvetica', 10)
    p.drawString(200, 60, 'THANK YOU FOR YOUR BUSSINESS!')'''


    #Boby
    p.setFillColor('#020000')
    p.setFont('Helvetica', 11)
    p.drawString(450, 150, "Subtotal: $" + str(invoice.subtotal))
    p.setFont('Helvetica', 11)
    p.drawString(450, 130, "7% FEE: $" + str(invoice.comission_fee))
    p.setFont('Helvetica', 11)
    p.drawString(450, 110, "WIRE FEE: $" + str(invoice.wire_fee))
    p.setFont('Helvetica', 11)
    p.drawString(450, 90, "ACH FEE: $" + str(invoice.ach_fee))
    p.setFont('Helvetica', 11)
    p.drawString(450, 70, "Others FEE: $" + str(invoice.discount))
    p.setFont('Helvetica-Bold', 12)
    p.drawString(450, 50, "Total: $" + str(invoice.total))

    styles = getSampleStyleSheet()
    stylesBH = styles["Heading3"]
    stylesBH.alignment = TA_CENTER
    stylesBH.fontSize = 10
    stylesBH.fill = '#34495E'
    broker = Paragraph('''Customer Name''', stylesBH)
    driver = Paragraph('''Driver''', stylesBH)
    pickupdate = Paragraph('''Pick Up Date''',stylesBH)
    pickupfrom = Paragraph('''Pick Up From''', stylesBH)
    deliver = Paragraph('''Deliver To''', stylesBH)
    loadno = Paragraph('''Load No.''', stylesBH)
    value = Paragraph('''Agreed Amount''', stylesBH)
    data = []
    data.append([broker, driver, pickupdate, pickupfrom, deliver, loadno, value])

    stylesBD = styles["BodyText"]
    stylesBD.alignment = TA_CENTER
    stylesBD.fontSize = 7
    high = 600
    for l in descrip:
        driver = DriversLogt.objects.get(id_dr=l.driver_id)
        colum1 = Paragraph(l.broker, stylesBD)
        colum2 = Paragraph(driver.name, stylesBD)
        colum3 = Paragraph(str(l.pickup_date), stylesBD)
        colum4 = Paragraph(l.pickup_from, stylesBD)
        colum5 = Paragraph(l.deliver, stylesBD)
        colum6 = Paragraph(l.number, stylesBD)
        colum7 = Paragraph(str(l.value), stylesBD)
        this_descrip = [colum1, colum2 , colum3 , colum4 , colum5 , colum6 , colum7]
        data.append(this_descrip)
        high = high - 18

    width, height = A4
    table = Table(data, colWidths=[3 * cm, 3 * cm, 2 * cm, 3 * cm, 3 * cm, 2 * cm, 2 * cm])
    table.setStyle(TableStyle([
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ]))
    table.wrapOn(p, width, height)
    table.drawOn(p, 40, high)

    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def PayDriverPDF(request, pk):
    payment = Payment.objects.get(id_sal=pk)
    payDriver = DriversHasPayment.objects.get(payments=payment)
    payLoad = PaymentHasLoad.objects.filter(payments=payment)
    driver = DriversLogt.objects.get(id_dr=payDriver.driver_id)
    descrip = []
    for l in payLoad:
        load = Load.objects.get(id_lod=l.loads_id)
        descrip.append(load)
    business = Busines.objects.get(id_bus=payment.business_id)
    response = HttpResponse(content_type='application/pdf')
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    # Header
    p.setFillColor('#2471A3')
    p.roundRect(0, 750, 694, 120, 20, fill=1)
    p.drawImage('static/img/truck.jpg', 440, 760, width=150, height=70)

    p.setFont('Helvetica', 16)
    p.setFillColor('#E5E7E9')
    p.drawCentredString(300, 785, business.name)
    if business.messager:
        p.setFont('Helvetica', 12)
        p.setFillColor('#E5E7E9')
        p.drawCentredString(300, 740, business.messager)

    p.setFont('Helvetica', 28)
    p.setFillColor('#E5E7E9')
    p.drawCentredString(70, 785, "INVOICE")

    p.setFillColor('#34495E')
    p.setFont('Helvetica-Bold', 12)
    p.drawString(410, 720, 'No: ' + str(payment.serial))

    p.setFont('Helvetica', 10)
    p.drawImage('static/img/icon/address-o.png', 50, 720, width=10, height=10)
    p.drawString(65, 720, business.address)
    p.drawImage('static/img/icon/phone-o.png', 50, 700, width=10, height=10)
    p.drawString(65, 700, business.phone)
    if business.fax:
        p.drawImage('static/img/icon/fax-o.png', 50, 680, width=10, height=10)
        p.drawString(65, 680, business.fax)

    p.setFont('Helvetica', 11)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(410, 700, 'Week Star Date: ' + str(payment.start_date))
    p.drawString(410, 680, 'Week End Date: ' + str(payment.end_date))

    # Driver
    if driver.type == 'Owner Operation':
      p.setFillColor('#34495E')
      p.setFont('Helvetica-Bold', 11)
      p.drawString(50, 620, 'To Pay Owner:')
      p.drawString(50, 570, 'To Pay Driver:')
      p.setFont('Helvetica', 11)
      p.drawString(75, 620, str(payDriver.total_owner))
      p.drawString(75, 570, str(payDriver.total_driver))
      if driver.owner_name:
        p.drawString(75, 630, driver.owner_name)
        p.drawString(50, 630, 'Owner Name:')
      if driver.name:
        p.drawString(75, 600, driver.name)

    if driver.type == 'Driver':
          p.setFillColor('#34495E')
          p.setFont('Helvetica-Bold', 11)
          p.drawString(50, 640, 'To Pay Owner:')
          p.drawString(50, 610, 'To Pay Driver:')
          p.setFont('Helvetica', 10)
          p.drawString(75, 625, '$'+str(payDriver.total_owner))
          if driver.name:
              p.setFont('Helvetica', 10)
              p.drawString(130, 610, driver.name)
          p.setFont('Helvetica-Bold', 12)
          p.setFillColor('#FE2E2E')
          p.drawString(75, 590, '$'+str(payDriver.total_driver))


    #Footer
    p.setFillColor('#2471A3')
    p.roundRect(0, 0, 694, 50, 0, fill=1)
    p.setFont('Helvetica', 9)
    p.setFillColorRGB(0, 0, 0)
    p.line(0, 50, 800, 50)
    user_print = ""
    if request.user.first_name:
        user_print = request.user.first_name+" "+request.user.last_name
    else:
        user_print= request.user.username
    p.drawString(30, 20, 'Date of printing '+time.strftime("%m/%d/%y %H:%M:%S")+' by %s' % user_print)
    p.setFillColor('#34495E')

    # Boby

    styles = getSampleStyleSheet()
    stylesBH = styles["Heading3"]
    stylesBH.alignment = TA_CENTER
    stylesBH.fontSize = 10
    stylesBH.fill = '#34495E'
    broker = Paragraph('''Broker''', stylesBH)
    pickupdate = Paragraph('''Pick Up Date''', stylesBH)
    pickupfrom = Paragraph('''Pick Up From''', stylesBH)
    deliverdate = Paragraph('''Deliver Date''', stylesBH)
    deliver = Paragraph('''Deliver To''', stylesBH)
    loadno = Paragraph('''Load No.''', stylesBH)
    value = Paragraph('''Agreed Amount''', stylesBH)
    data = []
    data.append([broker,loadno, pickupdate, pickupfrom, deliverdate, deliver, value])

    stylesBD = styles["BodyText"]
    stylesBD.alignment = TA_CENTER
    stylesBD.fontSize = 7
    high = 530
    for l in descrip:
        colum1 = Paragraph(l.broker, stylesBD)
        colum2 = Paragraph(l.number, stylesBD)
        colum3 = Paragraph(str(l.pickup_date), stylesBD)
        colum4 = Paragraph(l.pickup_from, stylesBD)
        colum5 = Paragraph(str(l.deliver_date), stylesBD)
        colum6 = Paragraph(l.deliver, stylesBD)
        colum7 = Paragraph(str(l.value), stylesBD)
        this_descrip = [colum1, colum2, colum3, colum4, colum5, colum6, colum7]
        data.append(this_descrip)
        high = high - 18
    width, height = A4
    table = Table(data, colWidths=[3 * cm, 3 * cm, 2 * cm, 3 * cm, 2 * cm, 3 * cm, 2 * cm])
    table.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ]))
    table.wrapOn(p, width, height)
    table.drawOn(p, 40, high)

    p.setFillColor('#58D3F7')
    p.roundRect(370, high - 30, 180, 20, 0, fill=1)
    p.setFillColor('#FAFAFA')
    p.roundRect(40, high - 175, 250, 160, 0, fill=1)
    p.setFillColor('#A9E2F3')
    p.roundRect(370, high - 70, 180, 40, 0, fill=1)
    p.setFillColor('#E0F2F7')
    p.roundRect(370, high - 195, 180, 125, 0, fill=1)
    p.setFillColor('#A9F5A9')
    p.roundRect(370, high - 220, 180, 25, 0, fill=1)
    p.setFillColor('#020000')
    p.setFont('Helvetica', 12)
    p.drawString(390, high - 25, "SUBTOTAL: $" + str(payment.gross))
    p.setFont('Helvetica', 10)
    p.drawString(50, high - 25, "NOTE:")
    p.drawString(50, high - 35, str(payment.note))
    p.drawString(390, high - 45, str(payDriver.porc_company) + "% COMPANY FEE: $" + str(payDriver.company_fee))
    p.drawString(390, high - 65, "GROSS: $" + str(payment.gross - payDriver.company_fee))
    p.drawString(390, high - 85, "PRE PASS: $" + str(payDriver.pre_pass))
    p.drawString(390, high - 105, "ESCROW: $" + str(payDriver.escrow))
    p.drawString(390, high - 125, "DOWN PAYMENT: $" + str(payDriver.down_payment))
    p.drawString(390, high - 145, "INSURANCE: $" + str(payDriver.insurance))
    p.drawString(390, high - 165, "DIESEL: $" + str(payDriver.diesel))
    p.drawString(390, high - 185, "Micellaneous: $" + str(payDriver.other))
    p.setFont('Helvetica-Bold', 12)
    p.drawString(390, high - 210, "Total: $" + str(payment.value))

    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def PayDispatchPDF(request, pk):
    payment = Payment.objects.get(id_sal=pk)
    payDispatch = DispatchHasPayment.objects.get(payments=payment)
    payLoad = PaymentHasLoad.objects.filter(payments=payment)
    dispatch = DispatchLogt.objects.get(id_dsp=payDispatch.dispatch_id)
    descrip = []
    for l in payLoad:
        load = Load.objects.get(id_lod=l.loads_id)
        descrip.append(load)
    business = Busines.objects.get(id_bus=payment.business_id)
    response = HttpResponse(content_type='application/pdf')
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    # Header
    p.setFillColor('#2471A3')
    p.roundRect(0, 750, 694, 120, 20, fill=1)
    p.drawImage('static/img/truck.jpg', 440, 760, width=150, height=70)

    p.setFont('Helvetica', 16)
    p.setFillColor('#E5E7E9')
    p.drawCentredString(300, 785, business.name)
    if business.messager:
        p.setFont('Helvetica', 12)
        p.setFillColor('#E5E7E9')
        p.drawCentredString(300, 740, business.messager)

    p.setFont('Helvetica', 28)
    p.setFillColor('#E5E7E9')
    p.drawCentredString(70, 785, "INVOICE")

    p.setFillColor('#34495E')
    p.setFont('Helvetica-Bold', 12)
    p.drawString(410, 720, 'No: ' + str(payment.serial))

    p.setFont('Helvetica', 10)
    p.drawImage('static/img/icon/address-o.png', 50, 720, width=10, height=10)
    p.drawString(65, 720, business.address)
    p.drawImage('static/img/icon/phone-o.png', 50, 700, width=10, height=10)
    p.drawString(65, 700, business.phone)
    if business.fax:
        p.drawImage('static/img/icon/fax-o.png', 50, 680, width=10, height=10)
        p.drawString(65, 680, business.fax)

    p.setFont('Helvetica', 11)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(410, 700, 'Week Star Date: ' + str(payment.start_date))
    p.drawString(410, 680, 'Week End Date: ' + str(payment.end_date))

    # Dispatch
    p.setFillColor('#34495E')
    p.setFont('Helvetica-Bold', 11)
    p.drawString(50, 620, 'Dispatch Name:')
    p.setFont('Helvetica', 10)
    p.drawString(140, 620, dispatch.name)

    # Footer
    p.setFillColor('#2471A3')
    p.roundRect(0, 0, 694, 50, 0, fill=1)
    p.setFont('Helvetica', 9)
    p.setFillColorRGB(0, 0, 0)
    p.line(0, 50, 800, 50)
    user_print = ""
    if request.user.first_name:
        user_print = request.user.first_name + " " + request.user.last_name
    else:
        user_print = request.user.username
    p.drawString(30, 20, 'Date of printing ' + time.strftime("%m/%d/%y %H:%M:%S") + ' by %s' % user_print)
    p.setFillColor('#34495E')


    # Boby
    styles = getSampleStyleSheet()
    stylesBH = styles["Heading3"]
    stylesBH.alignment = TA_CENTER
    stylesBH.fontSize = 10
    stylesBH.fill = '#34495E'
    broker = Paragraph('''Broker''', stylesBH)
    pickupdate = Paragraph('''Pick Up Date''', stylesBH)
    pickupfrom = Paragraph('''Pick Up From''', stylesBH)
    deliverdate = Paragraph('''Deliver Date''', stylesBH)
    deliver = Paragraph('''Deliver To''', stylesBH)
    loadno = Paragraph('''Load No.''', stylesBH)
    value = Paragraph('''Agreed Amount''', stylesBH)
    data = []
    data.append([broker, loadno, pickupdate, pickupfrom, deliverdate, deliver, value])

    stylesBD = styles["BodyText"]
    stylesBD.alignment = TA_CENTER
    stylesBD.fontSize = 7
    high = 530
    for l in descrip:
        colum1 = Paragraph(l.broker, stylesBD)
        colum2 = Paragraph(l.number, stylesBD)
        colum3 = Paragraph(str(l.pickup_date), stylesBD)
        colum4 = Paragraph(l.pickup_from, stylesBD)
        colum5 = Paragraph(str(l.deliver_date), stylesBD)
        colum6 = Paragraph(l.deliver, stylesBD)
        colum7 = Paragraph(str(l.value), stylesBD)
        this_descrip = [colum1, colum2, colum3, colum4, colum5, colum6, colum7]
        data.append(this_descrip)
        high = high - 18

    value_comission = (payment.gross * dispatch.comission) / 100
    p.setFillColor('#58D3F7')
    p.roundRect(370, high-30, 180, 20, 0, fill=1)
    p.setFillColor('#FAFAFA')
    p.roundRect(40, high - 135, 250, 120, 0, fill=1)
    p.setFillColor('#A9E2F3')
    p.roundRect(370, high-50, 180, 20, 0, fill=1)
    p.setFillColor('#E0F2F7')
    p.roundRect(370, high-70, 180, 20, 0, fill=1)
    p.setFillColor('#A9F5A9')
    p.roundRect(370, high-90, 180, 20, 0, fill=1)
    p.setFillColor('#020000')
    p.setFont('Helvetica', 12)
    p.drawString(390, high-25, "SUBTOTAL: $" + str(payment.gross))
    p.setFont('Helvetica', 10)
    p.drawString(50, high - 25, "NOTE:")
    p.drawString(50, high - 35, str(payment.note))
    p.drawString(390, high-45, str(dispatch.comission) + "% COMMISSION: $" + str(value_comission))
    p.drawString(390, high-65, "DISCOUNTS: $" + str(payment.discount))
    p.setFont('Helvetica-Bold', 12)
    p.drawString(390, high-85, "Total: $" + str(payment.value))
    width, height = A4
    table = Table(data, colWidths=[3 * cm, 3 * cm, 2 * cm, 3 * cm, 2 * cm, 3 * cm, 2 * cm])
    table.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ]))
    table.wrapOn(p, width, height)
    table.drawOn(p, 40, high)

    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def PayEmployeePDF(request, pk):
    payment = Payment.objects.get(id_sal = pk)
    payEmployee = EmployeeHasPayment.objects.get(payments=payment)
    employee = Employee.objects.get(id_emp=payEmployee.employee_id)
    response = HttpResponse(content_type='application/pdf')
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    #Header
    p.setFillColor('#2471A3')
    p.roundRect(0, 750, 694, 120, 20, fill=1)
    p.drawImage('static/img/logoFCI.png', 250, 760, width=150, height=70)

    p.setFont('Helvetica', 16)
    p.setFillColor('#34495E')
    p.drawCentredString(90, 700, "PAY STATEMENT ")


    p.setFont('Helvetica-Bold', 12)
    p.drawString(50, 680, 'No. '+str(payment.serial))

    p.setFont('Helvetica',12)
    p.setFillColorRGB(0,0,0)
    p.drawString(450, 700, 'Pay Date: '+str(payment.pay_date))
    p.line(450, 697, 562, 697)

    p.setFont('Helvetica', 10)
    p.drawImage('static/img/icon/address-o.png', 50, 650, width=10, height=10)
    p.drawString(65, 650, payment.business.address)
    p.drawImage('static/img/icon/phone-o.png', 50, 630, width=10, height=10)
    p.drawString(65, 630, payment.business.phone)
    if payment.business.fax:
        p.drawImage('static/img/icon/fax-o.png', 50, 610, width=10, height=10)
        p.drawString(65, 610, payment.business.fax)

    p.setFont('Helvetica', 11)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(400, 680, 'Period Star Date: ' + str(payment.start_date))
    p.drawString(400, 660, 'Period End Date: ' + str(payment.end_date))

    # Employee
    p.setFillColor('#34495E')
    p.setFont('Helvetica-Bold', 11)
    p.drawString(50, 580, 'Employee Name: ')
    p.setFont('Helvetica', 10)
    p.drawString(150, 580, employee.name+' '+employee.lastname)

    #Footer
    p.setFont('Helvetica', 9)
    p.setFillColorRGB(0, 0, 0)
    p.line(0, 50, 800, 50)
    p.drawString(30, 20, 'Date of printing '+time.strftime("%m/%d/%y %H:%M:%S")+' by %s' % request.user.first_name)

    #Boby
    # Employee
    if employee.type_salary == 'commission':
        sing = '%'
    else:
        sing = '$'
    p.setFillColor('#000000')
    p.setFont('Helvetica-Bold', 11)
    p.drawString(50, 550, 'Rate')
    p.setFont('Helvetica', 10)
    p.drawString(50, 530, sing+str(employee.value))
    if employee.type_salary == 'hour':
       p.setFillColor('#000000')
       p.setFont('Helvetica-Bold', 11)
       p.drawString(100, 550, 'Regular Hours')
       p.setFont('Helvetica', 10)
       p.drawString(100, 530, str(payment.regular_hours))

       p.setFillColor('#000000')
       p.setFont('Helvetica-Bold', 11)
       p.drawString(190, 550, 'Overtime Hours')
       p.setFont('Helvetica', 10)
       p.drawString(190, 530, str(payment.overtime_hours))

    p.setFillColor('#58D3F7')
    p.roundRect(370, 500, 180, 20, 0, fill=1)
    p.setFillColor('#FAFAFA')
    p.setFillColor('#A9E2F3')
    p.roundRect(370, 480, 180, 20, 0, fill=1)
    p.setFillColor('#A9F5A9')
    p.roundRect(370, 460, 180, 20, 0, fill=1)
    p.setFillColor('#020000')
    p.setFont('Helvetica', 12)
    p.drawString(390, 505, "GROSS: $" + str(payment.gross))
    p.setFont('Helvetica', 10)
    p.drawString(390, 485, "DISCOUNTS: $" + str(payment.discount))
    p.setFont('Helvetica-Bold', 12)
    p.drawString(390,465, "Total: $" + str(payment.value))
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
