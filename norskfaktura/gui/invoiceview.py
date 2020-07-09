
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from norskfaktura.gui import signaling

class InvoiceView(Gtk.Box):
    def __init__(self, window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.window = window
        self.customer = None

        #
        # Data members
        #

        self.invoice_item_store = Gtk.ListStore(str, str, str, str, str, str)


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

        self.customer_info_labels = [
            Gtk.Label("Customer name"),
            Gtk.Label("Org. no: xxx xxx xxx"),
            Gtk.Label("Blåklokkevegen 26"),
            Gtk.Label(""),
            Gtk.Label("2322 RIDABU"),
        ]

        for label in self.customer_info_labels:
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

        calendar = Gtk.Calendar()
        calendar.connect("day-selected", self.on_date_selection)
        delivery_data_box.pack_start(calendar, True, True, 0)
        

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
            ["Beskrivelse", "Pris", "Antall", "Rabatt %", "Mva %", "Beløp"]
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
        self.due_days_entry.set_text("14")
        self.due_days_entry.set_width_chars(3)
        due_box = Gtk.Box(spacing=5)
        due_box.pack_start(due_label, False, True, 0)
        due_box.pack_start(self.due_days_entry, True, True, 0)
        grid.attach(due_box, 0, 9, 2, 1)

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
        #self.remove_button.connect()
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

        post_button = Gtk.Button("Postér")

        pay_button = Gtk.Button("Betal")
        pay_button.set_sensitive(False)

        pdf_button = Gtk.Button("Lag PDF")
        pdf_button.set_sensitive(False)
        
        creditnote_button = Gtk.Button("Lag kreditnota")
        creditnote_button.set_sensitive(False)

        signaling.new("home-clicked", self) # signal to get back
        cancel_button = Gtk.Button("Avbryt")
        cancel_button.connect("clicked", self.on_cancel)

        for b in [
            post_button,
            pay_button,
            pdf_button,
            creditnote_button,
            cancel_button,
        ]:
            button_box.pack_start(b, False, True, 0)


    def _blank_item_input(self):
        for w in [
            self.description_entry,
            self.price_entry,
            self.amount_entry,
            self.discount_entry,
            self.vat_entry,
        ]:
            w.set_text("")

    def on_date_selection(self, calendar):
        date = calendar.get_date()
        day = pad_zeroes(date.day, 2)
        month = pad_zeroes(date.month, 2)
        self.delivery_date_entry.set_text(
            f"{day}.{month}.{date.year}"
        )

    def on_add_clicked(self, widget):
        self.invoice_item_store.append(
            [
                self.description_entry.get_text(),
                "asd",
                "asd",
                "asd",
                "asd",
                "asd",
            ]
        )
        print(self.customer)
        self._blank_item_input()
    
    def on_cancel(self, widget):
        self.emit("home-clicked", widget)

# For file naming and date formatting:
def pad_zeroes(n, padding): 
    """Returns string from number n, padded to lengt with leading zeroes"""
    if n - 10**(padding-1) >= 0: 
        return str(n) 
    else: 
        return f"0{pad_zeroes(n, padding-1)}" 
