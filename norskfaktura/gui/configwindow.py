import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from norskfaktura.gui import ConfigView

WINDOW_TITLE = "Norsk Faktura - oppsett"

class ConfigWindow(Gtk.Window):
    """Configuration window of the application.

    This window is shown when the configuration files doesn't exist as the
    application is starting. It contains a configuration view that the main
    window can reuse.
    """

    def __init__(self):
        Gtk.Window.__init__(self, title=WINDOW_TITLE)
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(100)

        self.main_view = ConfigView(self)
        self.stack.add_named(self.main_view, "main view")

        vbox.pack_start(self.stack, True, True, 0)


    def on_new_customer_clicked(self, *args):
        self.set_title("Ny kunde")
        self.customer_view.new_customer()
        self.stack.set_visible_child(self.customer_view)

def show_config_window():
    win = ConfigWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

