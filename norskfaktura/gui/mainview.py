import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject

from norskfaktura.gui import signaling

class MainView(Gtk.Box):
    def __init__(self, window, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.window = window

        signaling.new("customer-clicked", self)

        button = Gtk.Button("Kunde")
        button.connect("clicked", self.on_button_clicked)
        self.add(button)
    
    def on_button_clicked(self, widget):
        self.emit("customer-clicked", 42)
        self.window.set_title("Kunde")

