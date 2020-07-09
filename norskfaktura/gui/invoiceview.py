
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

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
        self.add(grid)


        # customer info
        self.customer_name = Gtk.Label("Customer name")
        self.customer_org = Gtk.Label("Org. no: xxx xxx xxx")
        self.customer_address1 = Gtk.Label("Blåklokkevegen 26")
        self.customer_address2 = Gtk.Label("")
        self.customer_postal = Gtk.Label("2322 RIDABU")


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
        self.add_button = Gtk.Button("Legg til")
        self.add_button.set_margin_left(12)
        self.add_button.connect("clicked", self.on_add_clicked)
        grid.attach(self.add_button, 8, 12, 1, 1)


    def _blank_item_input(self):
        for w in [
            self.description_entry,
            self.price_entry,
            self.amount_entry,
            self.discount_entry,
            self.vat_entry,
        ]:
            w.set_text("")

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