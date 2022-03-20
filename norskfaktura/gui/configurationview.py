from norskfaktura.gui import signaling
from gi.repository import Gtk, GObject
import gi
gi.require_version("Gtk", "3.0")


class ConfigView(Gtk.Box):
    """Configuration view of the application.

    This is a box that contains all the elements - and the layout - that
    the user sees when they are configuring the application. Be it in the Main
    window or the configuration window.
    """

    def __init__(self, window, *args, back_enabled=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.window = window
        self.set_orientation(Gtk.Orientation.VERTICAL)
        self.set_hexpand(True)
        self.set_vexpand(True)

        main_box = Gtk.Box()
        main_box.set_hexpand(True)
        main_box.set_vexpand(True)
        self.pack_start(main_box, True, False, 0)

        grid = Gtk.Grid()
        grid.set_hexpand(True)
        grid.set_vexpand(True)
        main_box.pack_start(grid, True, False, 0)


        horizontal_margin = 12
        vertical_margin = 12

        name_label = Gtk.Label("Navn: ")
        row = 0
        name_label.set_justify(Gtk.Justification.RIGHT)
        name_label.set_margin_left(horizontal_margin)
        name_label.set_margin_right(5)
        name_label.set_margin_top(horizontal_margin)
        grid.attach(name_label, 0, row, 1, 1)
        self.name_entry = Gtk.Entry()
        self.name_entry.set_width_chars(25)
        self.name_entry.set_margin_top(vertical_margin)
        grid.attach(self.name_entry, 1, row, 4, 1)

        org_label = Gtk.Label("Org. nr (om aktuelt): ")
        row += 1
        top_margin = 8
        org_label.set_justify(Gtk.Justification.RIGHT)
        org_label.set_margin_left(horizontal_margin)
        org_label.set_margin_right(5)
        org_label.set_margin_top(top_margin)
        grid.attach(org_label, 0, row, 1, 1)
        self.org_entry = Gtk.Entry()
        self.org_entry.set_margin_top(top_margin)
        self.org_entry.set_width_chars(25)
        grid.attach(self.org_entry, 1, row, 4, 1)

        phone_label = Gtk.Label("Telefon: ")
        row += 1
        phone_label.set_justify(Gtk.Justification.RIGHT)
        phone_label.set_margin_left(horizontal_margin)
        phone_label.set_margin_top(top_margin)
        phone_label.set_margin_right(5)
        grid.attach(phone_label, 0, row, 1, 1)
        self.phone_entry = Gtk.Entry()
        self.phone_entry.set_margin_top(top_margin)
        grid.attach(self.phone_entry, 1, row, 3, 1)

        email_label = Gtk.Label("Epost: ")
        row += 1
        email_label.set_justify(Gtk.Justification.RIGHT)
        email_label.set_margin_left(horizontal_margin)
        email_label.set_margin_right(5)
        grid.attach(email_label, 0, row, 1, 1)
        self.email_entry = Gtk.Entry()
        self.email_entry.set_margin_top(top_margin)
        self.email_entry.set_margin_bottom(vertical_margin)
        grid.attach(self.email_entry, 1, row, 3, 1)

        address_label = Gtk.Label("Adresse: ")
        row += 1
        address_label.set_justify(Gtk.Justification.RIGHT)
        address_label.set_margin_left(horizontal_margin)
        address_label.set_margin_right(5)
        address_label.set_margin_top(top_margin)
        grid.attach(address_label, 0, row, 1, 1)
        self.address_entry_one = Gtk.Entry()
        self.address_entry_one.set_width_chars(25)
        self.address_entry_one.set_margin_top(top_margin)
        grid.attach(self.address_entry_one, 1, row, 3, 1)
        row += 1
        top_margin = 6
        self.address_entry_two = Gtk.Entry()
        self.address_entry_two.set_width_chars(25)
        self.address_entry_two.set_margin_top(top_margin)
        grid.attach(self.address_entry_two, 1, row, 3, 1)
        
        postal_label = Gtk.Label("Postnr og sted: ")
        row += 1
        postal_label.set_justify(Gtk.Justification.RIGHT)
        postal_label.set_margin_left(horizontal_margin)
        postal_label.set_margin_right(5)
        postal_label.set_margin_top(top_margin)
        grid.attach(postal_label, 0, row, 1, 1)
        self.postal_entry = Gtk.Entry()
        self.postal_entry.set_margin_top(top_margin)
        self.postal_entry.set_margin_bottom(vertical_margin)
        grid.attach(self.postal_entry, 1, row, 3, 1)


        # invoice settings box
        label = Gtk.Label("Kontonr: ")
        right_row = 0
        label.set_justify(Gtk.Justification.RIGHT)
        label.set_margin_left(horizontal_margin*2)
        label.set_margin_right(horizontal_margin)
        label.set_margin_top(horizontal_margin)
        grid.attach(label, 5, right_row, 1, 1)
        self.account_entry = Gtk.Entry()
        self.account_entry.set_width_chars(25)
        self.account_entry.set_margin_top(vertical_margin)
        self.account_entry.set_margin_right(horizontal_margin*2)
        grid.attach(self.account_entry, 6, right_row, 4, 1)

        label = Gtk.Label("Betalingsfrist: ")
        top_margin = 8
        right_row += 1
        label.set_justify(Gtk.Justification.RIGHT)
        label.set_margin_left(horizontal_margin*2)
        label.set_margin_right(horizontal_margin)
        label.set_margin_top(top_margin)
        grid.attach(label, 5, right_row, 1, 1)

        box = Gtk.Box()
        grid.attach(box, 6, right_row, 3, 1)

        self.due_entry = Gtk.Entry()
        self.due_entry.set_width_chars(2)
        self.due_entry.set_margin_top(top_margin)
        box.pack_start(self.due_entry, True, True, 0)
        label = Gtk.Label("dager")
        label.set_justify(Gtk.Justification.LEFT)
        label.set_margin_top(top_margin)
        box.pack_start(label, True, True, 0)

        label = Gtk.Label("MVA-registrert: ")
        right_row += 1
        label.set_justify(Gtk.Justification.RIGHT)
        label.set_margin_left(horizontal_margin*2)
        label.set_margin_right(horizontal_margin)
        label.set_margin_top(top_margin)
        grid.attach(label, 5, right_row, 1, 1)
        self.vat_checkbox = Gtk.CheckButton()
        self.vat_checkbox.set_margin_top(top_margin)
        self.vat_checkbox.set_margin_right(horizontal_margin*2)
        grid.attach(self.vat_checkbox, 6, right_row, 4, 1)

        label = Gtk.Label("Logo: ")
        right_row += 2
        label.set_justify(Gtk.Justification.RIGHT)
        label.set_margin_left(horizontal_margin*2)
        label.set_margin_right(horizontal_margin)
        label.set_margin_top(top_margin)
        grid.attach(label, 5, right_row, 1, 1)

        box = Gtk.Box()
        grid.attach(box, 6, right_row, 3, 1)

        self.logo_entry = Gtk.Entry()
        self.logo_entry.set_margin_top(top_margin)
        self.browse_logo_button = Gtk.Button("Åpne")
        self.browse_logo_button.set_margin_left(4)
        self.browse_logo_button.set_margin_right(horizontal_margin*2)
        self.browse_logo_button.set_margin_top(top_margin)
        box.pack_start(self.logo_entry, True, True, 0)
        box.pack_start(self.browse_logo_button, True, True, 0)

        label = Gtk.Label("PDF-mappe: ")
        right_row += 1
        label.set_justify(Gtk.Justification.RIGHT)
        label.set_margin_left(horizontal_margin*2)
        label.set_margin_right(horizontal_margin)
        label.set_margin_top(top_margin)
        grid.attach(label, 5, right_row, 1, 1)

        box = Gtk.Box()
        grid.attach(box, 6, right_row, 3, 1)

        self.pdf_entry = Gtk.Entry()
        self.pdf_entry.set_margin_top(top_margin)
        self.browse_pdf_button = Gtk.Button("Åpne")
        self.browse_pdf_button.set_margin_left(4)
        self.browse_pdf_button.set_margin_right(horizontal_margin*2)
        self.browse_pdf_button.set_margin_top(top_margin)
        box.pack_start(self.pdf_entry, True, True, 0)
        box.pack_start(self.browse_pdf_button, True, True, 0)

        # buttons
        save_button = Gtk.Button("Lagre")
        row += 1
        vert_spacer = 20
        save_button.set_margin_right(horizontal_margin)
        save_button.set_margin_top(vert_spacer)
        save_button.set_margin_bottom(vertical_margin)
        save_button.connect("clicked", self.on_save_clicked)
        grid.attach(save_button, 7, row, 1, 1)

        self.back_button = Gtk.Button("Tilbake")
        self.back_button.set_margin_right(horizontal_margin*2)
        self.back_button.set_margin_top(vert_spacer)
        self.back_button.set_margin_bottom(vertical_margin)
        grid.attach(self.back_button, 8, row, 1, 1)
        self.back_button.set_sensitive(back_enabled)
        
        # creating and attaching signal to go home
        signaling.new("home-clicked", self) # signal to get back
        self.back_button.connect("clicked", self.on_back_clicked)



    def on_save_clicked(*args):
        pass

    def on_back_clicked(self, widget):
        self.emit("home-clicked", self)



    # templates for handlers

    def clear_search(self):
        self.customer_search_entry.set_text("")
        self.invoice_search_entry.set_text("")
        self.refresh_customers()
        self.refresh_invoices()



    def on_new_customer_clicked(self, widget):
        self.emit("new-customer-clicked", 42)


