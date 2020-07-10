import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from norskfaktura.gui import CustomerView, MainView, InvoiceView

WINDOW_TITLE = "Norsk Faktura"

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title=WINDOW_TITLE)
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(2000)

        self.main_view = MainView(self)
        self.stack.add_named(self.main_view, "main view")
        self.main_view.connect("customer-clicked", self.on_customer_clicked)

        self.customer_view = CustomerView(self)
        self.stack.add_named(self.customer_view, "customer view")
        self.customer_view.connect("home-clicked", self.on_home_clicked)
        self.customer_view.connect("new-invoice", self.on_new_invoice)

        self.invoice_view = InvoiceView(self)
        self.stack.add_named(self.invoice_view, "invoice view")
        self.invoice_view.connect("home-clicked", self.on_home_clicked)


        vbox.pack_start(self.stack, True, True, 0)


    def on_customer_clicked(self, *args):
        self.stack.set_visible_child(self.customer_view)

    def on_home_clicked(self, *args):
        self.stack.set_visible_child(self.main_view)
        self.set_title(WINDOW_TITLE)

    def on_new_invoice(self, *args):
        self.set_title("Ny faktura")
        self.invoice_view.new_invoice(args[-1])

        self.stack.set_visible_child(self.invoice_view)

def show_main_window():
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()