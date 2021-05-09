from norskfaktura.invoice import Invoice, get_invoice_by_id, get_due_invoices
from norskfaktura.customer import Customer, search_customers
from norskfaktura.gui import signaling
from gi.repository import Gtk, GObject
import gi
gi.require_version("Gtk", "3.0")


class MainView(Gtk.Box):
    """ Main view of the application.

    This is a box that contains all the elements - and the layout - that
    the user sees when they open the app (unless the configuration is
    missing). It is itself contained within the MainWindow, like most
    other views.
    """

    def __init__(self, window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.window = window
        self.set_orientation(Gtk.Orientation.VERTICAL)
        self.customers = None
        self.invoices = None

        # Customer section
        customer_box = Gtk.Box(spacing=8)
        #customer_buttonbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        customer_contentbox = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.pack_start(customer_box, True, True, 0)
        customer_box.pack_start(customer_contentbox, True, True, 0)
        #customer_box.pack_start(customer_buttonbox, True, True, 0)

           # Top pane (search)
        customer_top_pane = Gtk.Box(spacing=8)
        self.customer_search_entry = Gtk.Entry()
        customer_top_pane.pack_start(
            self.customer_search_entry, True, True, 0
        )
        self.customer_search_button = Gtk.Button("Kundesøk")
        self.customer_search_button.connect("clicked", self.refresh_customers)
        customer_top_pane.pack_start(
            self.customer_search_button, False, False, 0
        )
        customer_contentbox.pack_start(customer_top_pane, False, True, 0)

           # Beginning of customer listing
        customer_contentbox.pack_start(
            Gtk.Label("Kundeliste", margin_top=20, xalign=0),
            False,
            True,
            0
        )

           # Tree view of customers
        self.customer_store = Gtk.ListStore(int, str, str)
        self.customer_treeview = Gtk.TreeView.new_with_model(
            self.customer_store)
        signaling.new("customer-chosen", self)
        self.customer_treeview.connect(
            "row-activated", self.on_customer_select)
        for i, column_title in enumerate(
            ["Kundenr", "Navn", "Adresse"]
        ):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.customer_treeview.append_column(column)
        customer_scrolledwindow = Gtk.ScrolledWindow(
            vexpand=True,
            hexpand=True,
            min_content_width=100,
        )
        customer_scrolledwindow.add(self.customer_treeview)
        customer_contentbox.pack_start(
            customer_scrolledwindow, True, True, 0
        )

           # Buttons box
        signaling.new("new-customer-clicked", self)
        new_customer_button = Gtk.Button(
            "Ny kunde", margin_start=120)  # , margin_top=46)
        new_customer_button.connect("clicked", self.on_new_customer_clicked)
        customer_top_pane.pack_end(new_customer_button, False, True, 0)

        # Invoices section
        invoice_box = Gtk.Box(spacing=8)
        #invoice_buttonbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        invoice_contentbox = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.pack_start(invoice_box, True, True, 0)
        invoice_box.pack_start(invoice_contentbox, True, True, 0)
        #invoice_box.pack_start(invoice_buttonbox, True, True, 0)

           # Beginning of invoice listing
        invoice_contentbox.pack_start(
            Gtk.Label("Utestående fakturaer", margin_top=20, xalign=0),
            False,
            True,
            0
        )

           # Tree view of invoices
        self.invoice_store = Gtk.ListStore(int, str, str)
        self.invoice_treeview = Gtk.TreeView.new_with_model(self.invoice_store)
        signaling.new("invoice-chosen", self)
        self.invoice_treeview.connect("row-activated", self.on_invoice_select)
        for i, column_title in enumerate(
            ["Fakturanr", "Kunde", "Beløp"]
        ):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.invoice_treeview.append_column(column)
        invoice_scrolledwindow = Gtk.ScrolledWindow(
            vexpand=True,
            hexpand=True,
            min_content_width=100,
        )
        invoice_scrolledwindow.add(self.invoice_treeview)
        invoice_contentbox.pack_start(
            invoice_scrolledwindow, True, True, 0
        )

           # Old invoice retrieval
        invoice_contentbox.pack_start(
            Gtk.Label("Hent gammel faktura", xalign=0),
            False,
            False,
            0
        )

        invoice_search_pane = Gtk.Box(spacing=6)
        invoice_contentbox.pack_start(
            invoice_search_pane, False, False, 0
        )
        self.invoice_search_entry = Gtk.Entry()
        invoice_search_pane.pack_start(
            self.invoice_search_entry, False, False, 0
        )
        self.invoice_search_button = Gtk.Button("Nummersøk")
        signaling.new("invoice-search", self)
        self.invoice_search_button.connect("clicked", self.on_invoice_search)
        invoice_search_pane.pack_start(
            self.invoice_search_button, False, False, 0
        )

        # Filling treeviews
        self.refresh_customers()
        self.refresh_invoices()

    def clear_search(self):
        self.customer_search_entry.set_text("")
        self.invoice_search_entry.set_text("")
        self.refresh_customers()
        self.refresh_invoices()

    def refresh_customers(self, *args):
        customers = search_customers(self.customer_search_entry.get_text())
        self.customers = {elem.id: elem for elem in customers}
        self.customer_store.clear()
        for customer in customers:
            self.customer_store.append(
                [
                    customer.id,
                    customer.name,
                    customer.address_oneliner()
                ]
            )

    def refresh_invoices(self):
        invoices = get_due_invoices()
        self.invoices = {elem.id: elem for elem in invoices}
        self.invoice_store.clear()
        for invoice in invoices:
            vat, balance, total = invoice.get_totals()
            self.invoice_store.append(
                [
                    invoice.id,
                    invoice.customer.name,
                    total
                ]
            )

    def on_new_customer_clicked(self, widget):
        self.emit("new-customer-clicked", 42)

    def on_customer_select(self, *args):
        selection = self.customer_treeview.get_selection()
        model, list_iter = selection.get_selected()
        customer = None
        if list_iter != None:
            id = model[list_iter][0]
            customer = self.customers[id]

        self.emit("customer-chosen", customer)

    def on_invoice_select(self, *args):
        selection = self.invoice_treeview.get_selection()
        model, list_iter = selection.get_selected()
        invoice = None
        if list_iter != None:
            id = model[list_iter][0]
            invoice = self.invoices[id]

        self.emit("invoice-chosen", invoice)

    def on_invoice_search(self, *args):
        self.emit("invoice-search", self.invoice_search_entry.get_text())
