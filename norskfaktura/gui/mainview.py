import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject

from norskfaktura.gui import signaling

class MainView(Gtk.Box):
    def __init__(self, window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.window = window
        self.set_orientation(Gtk.Orientation.VERTICAL)

        # Customer section
        customer_box = Gtk.Box(spacing=8)
        #customer_buttonbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        customer_contentbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
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
        self.customer_treeview = Gtk.TreeView.new_with_model(self.customer_store)
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
        new_customer_button = Gtk.Button("Ny kunde", margin_start=120)#, margin_top=46)
        new_customer_button.connect("clicked", self.on_new_customer_clicked)
        customer_top_pane.pack_end(new_customer_button, False,True, 0)

        # Invoices section
        invoice_box = Gtk.Box(spacing=8)
        #invoice_buttonbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        invoice_contentbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
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
        invoice_search_pane.pack_start(
            self.invoice_search_button, False, False, 0
        )

    
    def on_new_customer_clicked(self, widget):
        self.emit("new-customer-clicked", 42)

