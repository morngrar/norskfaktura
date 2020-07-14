
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from norskfaktura.gui import signaling
from norskfaktura import invoice as inv
from norskfaktura.config import load_config
from norskfaktura.common import pad_zeroes

class InvoiceView(Gtk.Box):
    def __init__(self, window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.window = window
        self.customer = None

        #
        # Data members
        #

        self.invoice_item_store = Gtk.ListStore(int, str, str, str, str, str, str)


        #
        # Setting up the widgets
        # 

        # Setting up the grid in which the elements are to be positionned
        grid = Gtk.Grid()
        grid.set_row_homogeneous(True)
        self.set_orientation(Gtk.Orientation.VERTICAL)
        self.set_spacing = 6
        self.pack_end(grid, True, True, 0)


        # customer info
        customer_box = Gtk.Box()
        address_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        customer_box.pack_start(address_box, True, True, 0)
        self.pack_start(customer_box, True, True, 0)

        self.customer_info_labels = {
            "name" : Gtk.Label("Customer name"),
            "org" : Gtk.Label("Org. no: xxx xxx xxx"),
            "addr" : [
                Gtk.Label("Blåklokkevegen 26"),
                Gtk.Label(""),
                Gtk.Label("2322 RIDABU"),
            ]
        }

        #packing first two fields
        for label in list(self.customer_info_labels.values())[:-1]:
            label.set_xalign(0)
            address_box.pack_start(label, False, True, 6)

        for label in self.customer_info_labels["addr"]:
            label.set_xalign(0)
            address_box.pack_start(label, False, True, 6)

        # Delivery info
        delivery_frame = Gtk.Frame.new("Leveranseinfo")
        
        delivery_data_box = Gtk.Box(spacing=6)
        delivery_entry_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        delivery_data_box.pack_start(delivery_entry_box, True, True, 0)

        delivery_date_label = Gtk.Label("Leveringsdato")
        delivery_date_label.set_xalign(0)
        delivery_entry_box.pack_start(
            delivery_date_label,
            True, True, 0
        )
        self.delivery_date_entry = Gtk.Entry()
        self.delivery_date_entry.set_width_chars(10)
        delivery_entry_box.pack_start(self.delivery_date_entry, True, True, 0)

        delivery_address_label = Gtk.Label("Addresse")
        delivery_address_label.set_xalign(0)
        delivery_entry_box.pack_start(
            delivery_address_label,
            True, True, 0
        )

        self.delivery_address_fields = [
            Gtk.Entry() for i in range(3)
        ]

        for entry in self.delivery_address_fields:
            delivery_entry_box.pack_start(entry, True, True, 0)

        self.calendar = Gtk.Calendar()
        self.calendar.connect("day-selected", self.on_date_selection)
        delivery_data_box.pack_start(self.calendar, True, True, 0)
        

        delivery_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        delivery_box.set_margin_left(6)
        delivery_box.set_margin_right(6)
        delivery_box.set_margin_bottom(6)
        delivery_box.pack_start(delivery_data_box, True, True, 0)
        delivery_frame.add(delivery_box)
        customer_box.pack_start(delivery_frame, True, True, 0)

        # Box for message
        message_box = Gtk.Box()
        message_box.set_margin_top(12)
        self.pack_start(message_box, True, True, 0)
        message_label = Gtk.Label("Melding:")
        self.message_entry = Gtk.Entry()
        message_box.pack_start(message_label, False, False, 5)
        message_box.pack_start(self.message_entry, True, True, 0)


        # creating the treeview
        self.treeview = Gtk.TreeView.new_with_model(self.invoice_item_store)
        for i, column_title in enumerate(
            ["#", "Beskrivelse", "Pris", "Antall", "Rabatt %", "Mva %", "Beløp"]
        ):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)

        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.scrollable_treelist.set_hexpand(True) # will expand horizontally if resized
        grid.attach(self.scrollable_treelist, 0, 0, 8, 9)

        self.scrollable_treelist.add(self.treeview)
        self.scrollable_treelist.set_margin_bottom(6)
        self.scrollable_treelist.set_margin_top(12)

        # Days until due fields
        due_label = Gtk.Label("Antall dager til forfall:")
        self.due_days_entry = Gtk.Entry()
        self.due_days_entry.set_width_chars(3)
        due_box = Gtk.Box(spacing=5)
        due_box.pack_start(due_label, False, True, 0)
        due_box.pack_start(self.due_days_entry, True, True, 0)
        grid.attach(due_box, 0, 9, 2, 1)

        # Customer balance fields
        customer_balance_label = Gtk.Label("Allerede betalt av kunde:")
        self.customer_balance_entry = Gtk.Entry()
        self.customer_balance_entry.set_width_chars(6)
        balance_box = Gtk.Box(spacing=5)
        balance_box.pack_start(customer_balance_label, False, True, 0)
        balance_box.pack_start(self.customer_balance_entry, True, True, 0)
        grid.attach(balance_box, 0, 10, 2, 1)

        # Summary below treeview
        total_vat_label = Gtk.Label("Herav Mva:")
        total_vat_label.set_xalign(1)
        total_vat_label.set_margin_right(6)
        grid.attach(total_vat_label, 5, 9, 1, 1)
        self.total_vat_value = Gtk.Label("999,99")
        self.total_vat_value.set_xalign(1)
        grid.attach(self.total_vat_value, 6, 9, 1, 1)

        total_label = Gtk.Label()
        total_label.set_markup("<b>Totalt:</b>")
        total_label.set_xalign(1)
        total_label.set_margin_right(6)
        total_label.set_margin_bottom(12)
        grid.attach(total_label, 5, 10, 1, 1)
        self.total_value = Gtk.Label()
        self.total_value.set_markup("<b>4999,99</b>")
        self.total_value.set_xalign(1)
        grid.attach(self.total_value, 6, 10, 1, 1)
        self.total_value.set_margin_bottom(12)

        # edit fields below summary
        description_label = Gtk.Label("Beskrivelse")
        description_label.set_xalign(0)
        grid.attach(description_label, 0, 11, 3, 1)
        self.description_entry = Gtk.Entry()
        self.description_entry.set_width_chars(25)
        grid.attach(self.description_entry, 0, 12, 3, 1)

        price_label = Gtk.Label("Pris")
        price_label.set_xalign(0)
        grid.attach(price_label, 3, 11, 1, 1)
        self.price_entry = Gtk.Entry()
        self.price_entry.set_width_chars(9)
        grid.attach(self.price_entry, 3, 12, 1, 1)

        amount_label = Gtk.Label("Antall")
        amount_label.set_xalign(0)
        grid.attach(amount_label, 4, 11, 1, 1)
        self.amount_entry = Gtk.Entry()
        self.amount_entry.set_width_chars(3)
        grid.attach(self.amount_entry, 4, 12, 1, 1)

        discount_label = Gtk.Label("Rabatt %")
        discount_label.set_xalign(0)
        grid.attach(discount_label, 5, 11, 1, 1)
        self.discount_entry = Gtk.Entry()
        self.discount_entry.set_width_chars(2)
        grid.attach(self.discount_entry, 5, 12, 1, 1)

        vat_label = Gtk.Label("Mva %")
        vat_label.set_xalign(0)
        grid.attach(vat_label, 6, 11, 1, 1)
        self.vat_entry = Gtk.Entry()
        self.vat_entry.set_width_chars(2)
        grid.attach(self.vat_entry, 6, 12, 1, 1)

        # Buttons
        self.remove_button = Gtk.Button("Fjern valgt rad")
        self.remove_button.set_margin_left(12)
        self.remove_button.connect("clicked", self.on_remove_row)
        grid.attach(self.remove_button, 8, 11, 1, 1)

        self.add_button = Gtk.Button("Legg til")
        self.add_button.set_margin_left(12)
        self.add_button.connect("clicked", self.on_add_clicked)
        grid.attach(self.add_button, 8, 12, 1, 1)


        # Button box besides invoice lines
        button_box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6,
        )
        button_box.set_margin_left(6)
        button_box.set_margin_top(12)
        button_box.set_margin_bottom(6)
        grid.attach(button_box, 8, 0, 1, 9)

        self.post_button = Gtk.Button("Postér")
        self.post_button.connect("clicked", self.on_post_clicked)

        self.pay_button = Gtk.Button("Betal")
        self.pay_button.set_sensitive(False)
        self.pay_button.connect("clicked", self.on_pay_clicked)

        self.pdf_button = Gtk.Button("Lag PDF")
        self.pdf_button.set_sensitive(False)
        self.pdf_button.connect("clicked", self.on_pdf_clicked)
        
        self.creditnote_button = Gtk.Button("Lag kreditnota")
        self.creditnote_button.set_sensitive(False)
        self.creditnote_button.connect("clicked", self.on_creditnote_clicked)

        signaling.new("home-clicked", self) # signal to get back
        cancel_button = Gtk.Button("Avbryt")
        cancel_button.connect("clicked", self.on_cancel)

        for b in [
            self.post_button,
            self.pay_button,
            self.pdf_button,
            self.creditnote_button,
            cancel_button,
        ]:
            button_box.pack_start(b, False, True, 0)

    def set_invoice(self, invoice):
        self.invoice = invoice
        self._refresh_rows()
        self._blank_item_input()
        if invoice.message:
            self.message_entry.set_text(self.invoice.message)
        else:
            self.message_entry.set_text("")

        delivery_date = [int(e) for e in self.invoice.delivery_date.split(".")]
        
        self.calendar.select_month(delivery_date[1]-1, delivery_date[2])
        self.calendar.select_day(delivery_date[0])
        self.delivery_date_entry.set_text(self.invoice.delivery_date)
        for i in range(3):
            self.delivery_address_fields[i].set_text(self.invoice.delivery_address[i])
        self._write_protect(True)
        self.customer_info_labels["name"].set_text(invoice.customer.name)
        self.customer_info_labels["org"].set_text(invoice.customer.org_no)
        for i in range(3):
            self.customer_info_labels["addr"][i].set_text(invoice.customer.address_lines[i])
        self.invoice.calculate_sums()
        vat, balance, total = self.invoice.get_totals()

        self.total_vat_value.set_text(vat)
        self.total_value.set_markup(f"<b>{total}</b>")
        self.customer_balance_entry.set_text(balance)
        self.due_days_entry.set_text(
            str((invoice.due - invoice.date).days)
        )
        self._set_button_sensitivity()
        

    def on_pay_clicked(self, widget):
        dialog = Gtk.MessageDialog(
            self.window,
            0,
            Gtk.MessageType.WARNING,
            Gtk.ButtonsType.OK_CANCEL,
            "Betale faktura",
        )
        dialog.format_secondary_text(
            "Du er i ferd med å sette denne fakturan som betalt, "
            "den vil da forsvinne fra oversikten over utestående fakturaer."
        )
        response = dialog.run()
        dialog.destroy()
        if response == Gtk.ResponseType.CANCEL:
            return

        self.invoice.pay()
        self._set_button_sensitivity()

    def on_pdf_clicked(self, widget):
        from norskfaktura.pdf import create_pdf
        create_pdf(self.invoice)

    def on_creditnote_clicked(self, widget):
        """Generates a new invoice which is inverse of the current one"""
        self.window.set_title(f"Ny Kreditnota for faktura nr {self.invoice.id}")
        self.invoice = inv.CreditNote(self.invoice)
        self._set_button_sensitivity()
        self._write_protect(True)
        self.message_entry.set_sensitive(True)  # should be able to change message
        self.invoice_item_store.clear()
        for row in self.invoice.get_gui_rows():
            self.invoice_item_store.append(row)

        vat, balance, total = self.invoice.get_totals()
        self.total_vat_value.set_text(vat)
        self.total_value.set_markup(f"<b>{total}</b>")
        self.customer_balance_entry.set_text(balance)

    def _blank_item_input(self):
        for w in [
            self.description_entry,
            self.price_entry,
        ]:
            w.set_text("")
        self.amount_entry.set_text("1")

        self.discount_entry.set_text("0")  # when discounts are added, take it from customer
        config = load_config()
        if config["firma"].getboolean("mva-registrert"):
            self.vat_entry.set_text("25")
        else:
            self.vat_entry.set_text("0")

    def on_date_selection(self, calendar):
        date = calendar.get_date()
        day = pad_zeroes(date.day, 2)
        month = pad_zeroes(date.month+1, 2)
        self.delivery_date_entry.set_text(
            f"{day}.{month}.{date.year}"
        )

    def on_add_clicked(self, widget):
        row = self.invoice.add_row(
            [
                self.description_entry.get_text(),
                self.price_entry.get_text(),
                self.amount_entry.get_text(),
                self.discount_entry.get_text(),
                self.vat_entry.get_text()
            ]
        )
        self.invoice_item_store.append(row)
        self.invoice.set_customer_balance(self.customer_balance_entry.get_text())
        vat, balance, total = self.invoice.get_totals()
        self.total_vat_value.set_text(vat)
        self.total_value.set_markup(f"<b>{total}</b>")
        self._blank_item_input()

    def on_remove_row(self, widget):
        selection = self.treeview.get_selection()
        model,list_iter = selection.get_selected()
        if list_iter != None:
            index = model[list_iter][0] - 1
            self.invoice.remove_row(index)
        self._refresh_rows()
    
    def _refresh_rows(self):
        self.invoice_item_store.clear()
        for row in self.invoice.get_gui_rows():
            self.invoice_item_store.append(row)

    def on_post_clicked(self, widget):
        if not self.invoice.rows:
            #dialog
            dialog = Gtk.MessageDialog(
                self.window,
                0,
                Gtk.MessageType.ERROR,
                Gtk.ButtonsType.CANCEL,
                "Tom faktura!",
            )
            dialog.format_secondary_text(
                "En faktura må ha rader for å kunne posteres."
            )
            dialog.run()
            dialog.destroy()
            return
        

        if self.invoice.has_flag(inv.CREDIT_NOTE):
            dialog_title = "Postere kreditnota"
            dialog_message = (
                "Er du sikker på at du vil postere? Dette vil kansellere den "
                "opprinnelige fakturaen, og den vil forsvinne fra oversikten "
                "over utestående fakturaer. Kreditnotaen kan ikke endres eller "
                "slettes etter dette."
            )
        else:
            dialog_title = "Postere faktura"
            dialog_message = (
                "Er du sikker på at du vil postere? Fakturaen kan ikke endres etterpå."
            )

        dialog = Gtk.MessageDialog(
            self.window,
            0,
            Gtk.MessageType.WARNING,
            Gtk.ButtonsType.OK_CANCEL,
            dialog_title,
        )
        dialog.format_secondary_text(dialog_message)
        response = dialog.run()
        dialog.destroy()
        if response == Gtk.ResponseType.CANCEL:
            return

        self.invoice.delivery_date = self.delivery_date_entry.get_text()
        self.invoice.message = self.message_entry.get_text()
        self.invoice.set_due_date(int(self.due_days_entry.get_text()))
        self.invoice.delivery_address = [
            field.get_text() for field in self.delivery_address_fields
        ]
        self.invoice.set_customer_balance(self.customer_balance_entry.get_text())



        self.invoice.post()

        # set buttons according to state
        self._set_button_sensitivity()

        self.window.set_title(f"Faktura nr {self.invoice.id}")

    def _write_protect(self, boolean):
        """Disables or enables editing widgets"""
        boolean = not boolean
        for widget in [
            self.delivery_date_entry,
            self.calendar,
            self.description_entry,
            self.amount_entry,
            self.discount_entry,
            self.due_days_entry,
            self.message_entry,
            self.price_entry,
            self.vat_entry,
            self.add_button,
            self.remove_button,
            self.customer_balance_entry,
        ]:
            widget.set_sensitive(boolean)


        for entry in self.delivery_address_fields:
            entry.set_sensitive(boolean)
    
    def _set_button_sensitivity(self):
        for button in [
            self.pdf_button,
            self.pay_button,
            self.creditnote_button,
        ]:
            button.set_sensitive(False)
        
        self.post_button.set_sensitive(True)



        if self.invoice.has_flag(inv.POSTED):
            self.post_button.set_sensitive(False)
            self._write_protect(True)

        if self.invoice.flags == inv.POSTED:  # if posted, unpaid and not cancelled
            self.pay_button.set_sensitive(True)
            self.creditnote_button.set_sensitive(True)

        
        if self.invoice.has_flags(inv.POSTED | inv.PAID):
            self.post_button.set_sensitive(False)
            self.pay_button.set_sensitive(False)

        if self.invoice.has_flags(
            inv.POSTED
        ) and not self.invoice.has_flag(
            inv.CANCELLED | inv.CREDIT_NOTE
        ):
            self.creditnote_button.set_sensitive(True)

        if self.invoice.has_flag(inv.POSTED):
            self.pdf_button.set_sensitive(True)

        
    
    def on_cancel(self, widget):
        self.emit("home-clicked", widget)

    def new_invoice(self, customer):
        """Resets view with fresh invoice for given customer"""
        self.invoice = inv.Invoice(customer)
        self._blank_item_input()
        self.calendar.select_month(self.invoice.date.month-1, self.invoice.date.year)
        self.calendar.select_day(self.invoice.date.day)
        for i in range(3):
            self.delivery_address_fields[i].set_text(self.invoice.delivery_address[i])
        self.invoice_item_store.clear()
        self.customer_info_labels["name"].set_text(customer.name)
        self.customer_info_labels["org"].set_text(customer.org_no)
        for i in range(3):
            self.customer_info_labels["addr"][i].set_text(customer.address_lines[i])
        self.total_vat_value.set_text("0,00")
        self.total_value.set_markup("<b>0,00</b>")
        config = load_config()
        self.due_days_entry.set_text(config['faktura']['betalingsfrist i dager'])
        self._set_button_sensitivity()
        self._write_protect(False)
        self.message_entry.set_text("")
        self.customer_balance_entry.set_text("0")

        


