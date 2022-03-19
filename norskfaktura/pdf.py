from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.platypus import Table, TableStyle, Image, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import os

from norskfaktura import common
from norskfaktura.config import load_config
from norskfaktura import invoice as inv



def create_pdf(invoice):
    """Creates a PDF-file from the given invoice object, and presents it"""

    # config parameters
    config = load_config()
    pdf_directory = config['miljø']['pdfmappe']
    logo_path = config['miljø']['logofil']
    company = config['firma']

    # Load fonts
    font_dir = os.path.join(common.HOST_DIR, "fonts")
    pdfmetrics.registerFont(TTFont("Courier Prime Bold", os.path.join(font_dir, "courier_prime/Courier Prime Bold.ttf")))
    pdfmetrics.registerFont(TTFont("Courier Prime Regular", os.path.join(font_dir, "courier_prime/Courier Prime.ttf")))
    pdfmetrics.registerFont(TTFont("Clear Sans Regular", os.path.join(font_dir, "clear_sans/ClearSans-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("Clear Sans Bold", os.path.join(font_dir, "clear_sans/ClearSans-Bold.ttf")))

    #
    # Generate pdf
    #

    # create file
    if pdf_directory:
        pdf_directory = os.path.expanduser(pdf_directory)
    else:
        pdf_directory = os.path.expanduser("~/.config/norskfaktura/")
    filename = os.path.join(pdf_directory, f"{common.pad_zeroes(invoice.id, 6)}.pdf")

    pdf = SimpleDocTemplate(
        filename,
        title=f"{company['navn']} - faktura nr {invoice.id}",
        pagesize=A4,
        leftmargin=1*cm,
        rightmargin=1*cm,
        topmargin=0
    )

    # logo and message
    if logo_path:
        logo_path = os.path.expanduser(logo_path)
        img = Image(logo_path, 5*cm, 2.5*cm)
    else:
        img = None
    styles = getSampleStyleSheet()
    message = Paragraph(f"<para>{invoice.message}</para>", styles["BodyText"])

    # Customer and Firm table
    invoice_type = "FAKTURA"
    if invoice.has_flag(inv.CREDIT_NOTE):
        invoice_type = "KREDITNOTA"

    data = [
        [img, "", "", invoice_type],
        ["", "", "", company['navn']],
        ["", "", "", company['adresse linje 1']],
    ]

    addr_two = company['adresse linje 2']
    if addr_two:
        data += [
            ['', '', '', addr_two],
            ["", "", "", company['postnr og sted']],
        ]
    else:
        data += [
            ["", "", "", company['postnr og sted']],
        ]

    customer_org_no = None
    if invoice.customer.org_no:
        customer_org_no = f"Org. nr: {invoice.customer.org_no}"


    date = invoice.date.strftime("%d.%m.%Y")
    due = invoice.due.strftime("%d.%m.%Y")

    data += [
        ["", "", "Org nr:", company['org. nr']],
        [invoice.customer.name, "", "Tlf:", company['tlf']],
        [invoice.customer.address_lines[0], "", "Epost:", company['epost']],
        [invoice.customer.address_lines[1], "", "Leveringsdato:", invoice.delivery_date],
        [invoice.customer.address_lines[2], "", "Levert til:", invoice.delivery_address[0]],
        [customer_org_no, "", "", invoice.delivery_address[1]],
        [message, "", "", invoice.delivery_address[2]],
        ["", "", "Fakturadato:", date],
        ["", "", "Fakturanummer:", invoice.id],
        ["", "", "Betalingsfrist:", due],
    ]
    addresses = Table(data, colWidths=[7*cm, 3*cm, 4*cm, 4*cm])

    # add styling to addressing fields
    style = TableStyle([

        # Header text
        ('FONTNAME', (0,0), (-1,0), 'Courier Prime Bold'),
        ('FONTSIZE', (0,0), (-1,0), 18),
        ("BOTTOMPADDING", (-1,0), (-1,0), 12),

        ('FONTSIZE', (-1,1), (-1,3), 12),
        ("BOTTOMPADDING", (0,3), (-1,3), 12),
        ('FONTNAME', (0,-2), (-1,-1), 'Clear Sans Bold'),

        # image spanning
        ("SPAN", (0,0), (0,3)),

        # message spanning
        ("SPAN", (0,-4), (1,-1)),

        # right-align labels
        ("ALIGN", (-2,0), (-2,-1), "RIGHT")
    ])
    addresses.setStyle(style)


    # Specification table
    data = [
        ['Beskrivelse', 'Pris', 'Antall', "Rabatt", "Mva", 'Beløp' ],
    ]

    for row in invoice.get_gui_rows():
        data.append(
            [row[1], row[2], row[3], f"{row[4]}%", f"{row[5]}%", f"{row[6]} kr"]
        )
    if invoice.has_flag(inv.CREDIT_NOTE):
        invoice.total = invoice.total * -1
    vat, balance, total = invoice.get_totals()
    if invoice.has_flag(inv.CREDIT_NOTE):
        invoice.calculate_sums()
    if invoice.has_flag(inv.CREDIT_NOTE):
        post_note = f"Dette dokumentet OPPHEVER tidligere faktura nr {invoice.credit_ref}"
        total_label = "TIL GODE:"
    else:
        post_note = "Vennligst oppgi fakturanummer ved betaling."
        total_label = "Å betale:"

    data += [
        ["", "", "", "Herav Mva:", "", f"{vat} kr"],
        ["", "", "", "Allerede betalt:", "", f"{balance} kr"],
        [post_note, "", "", total_label, "", f"{total} kr"],
    ]

    if not invoice.has_flag(inv.CREDIT_NOTE):
        data.append(
            ["", "", "", "Kontonr:", "", company['kontonummer']]
        )
    else:
        data.append(["", "", "", "", "", ""])

    specification = Table(data)

    # add styling to specification
    style = TableStyle([
        ('FONTNAME', (0,0), (-1,0), 'Courier Prime Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'Courier Prime Regular'),
        ('FONTNAME', (0,-2), (-1,-1), 'Clear Sans Bold'),
        ("SPAN", (0,-2), (1,-2)),
        ("SPAN", (-3,-3), (-2,-3)),
        ("SPAN", (-3,-2), (-2,-2)),
        ("SPAN", (-3,-1), (-2,-1)),
        ('ALIGN',(1,0),(1,-1),'RIGHT'),
        ('ALIGN',(2,0),(4,-4),'CENTER'),
        ('ALIGN',(-2,0),(-1,-1),'RIGHT'),
        ('ALIGN',(-3,-3),(-3,-1),'LEFT'),
        ('LINEBELOW',(0,0),(-1,0),1,colors.black),
        ('LINEABOVE',(0,-4),(-1,-4),1,colors.black),
    ])
    specification.setStyle(style)

    story = [
        addresses,
        Spacer(1, 0.5*cm),
        specification,
    ]

    pdf.build(story)

    os.system(f"xdg-open {filename} &")

