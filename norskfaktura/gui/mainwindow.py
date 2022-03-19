import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from norskfaktura.gui import CustomerView, MainView, InvoiceView

WINDOW_TITLE = "Norsk Faktura"

class MainWindow(Gtk.Window):
    """Main window of the application.

    This is the window which holds most of the applications 'views', which
    are simply boxes which contain widgets and layouts and functionality.
    The OS window remains the same, and the child views are switched aout
    as the user navigates between them.
    """

    def __init__(self):
        Gtk.Window.__init__(self, title=WINDOW_TITLE)
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(100)

        self.main_view = MainView(self)
        self.stack.add_named(self.main_view, "main view")
        self.main_view.connect("new-customer-clicked", self.on_new_customer_clicked)
        self.main_view.connect("customer-chosen", self.on_customer_chosen)
        self.main_view.connect("invoice-chosen", self.on_invoice_chosen)
        self.main_view.connect("invoice-search", self.on_invoice_search)

        self.customer_view = CustomerView(self)
        self.stack.add_named(self.customer_view, "customer view")
        self.customer_view.connect("home-clicked", self.on_home_clicked)
        self.customer_view.connect("new-invoice", self.on_new_invoice)

        self.invoice_view = InvoiceView(self)
        self.stack.add_named(self.invoice_view, "invoice view")
        self.invoice_view.connect("home-clicked", self.on_home_clicked)


        vbox.pack_start(self.stack, True, True, 0)


    def on_new_customer_clicked(self, *args):
        self.set_title("Ny kunde")
        self.customer_view.new_customer()
        self.stack.set_visible_child(self.customer_view)

    def on_customer_chosen(self, *args):
        customer = args[-1]
        self.set_title(f"Kunde - {customer.name}")
        self.customer_view.set_customer(customer)
        self.stack.set_visible_child(self.customer_view)

    def on_invoice_chosen(self, *args):
        invoice = args[-1]
        self.set_title(f"Faktura nr {invoice.id}")
        self.invoice_view.set_invoice(invoice)
        self.stack.set_visible_child(self.invoice_view)

    def on_home_clicked(self, *args):
        self.main_view.clear_search()
        self.stack.set_visible_child(self.main_view)
        self.set_title(WINDOW_TITLE)

    def on_new_invoice(self, *args):
        self.set_title("Ny faktura")
        self.invoice_view.new_invoice(args[-1])

        self.stack.set_visible_child(self.invoice_view)

    def on_invoice_search(self, *args):
        from norskfaktura.invoice import get_invoice_by_id
        invoice = get_invoice_by_id(int(args[-1]))
        if invoice:
            self.set_title(f"Faktura nr {invoice.id}")
            self.invoice_view.set_invoice(invoice)
            self.stack.set_visible_child(self.invoice_view)

def show_main_window():
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
