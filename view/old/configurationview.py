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
        self.back_enabled = back_enabled
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
        grid.attach(self.email_entry, 1, row, 3, 1)

        label = Gtk.Label("Webside: ")
        row += 1
        label.set_justify(Gtk.Justification.RIGHT)
        label.set_margin_left(horizontal_margin)
        label.set_margin_right(5)
        grid.attach(label, 0, row, 1, 1)
        self.website_entry = Gtk.Entry()
        self.website_entry.set_margin_top(top_margin)
        self.website_entry.set_margin_bottom(vertical_margin)
        grid.attach(self.website_entry, 1, row, 3, 1)

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


        label = Gtk.Label("Første faktura: ")
        right_row += 1
        label.set_justify(Gtk.Justification.RIGHT)
        label.set_margin_left(horizontal_margin)
        label.set_margin_top(top_margin)
        grid.attach(label, 5, right_row, 1, 1)
        self.first_no_entry = Gtk.Entry()
        self.first_no_entry.set_margin_top(top_margin)
        self.first_no_entry.set_margin_right(170)
        grid.attach(self.first_no_entry, 6, right_row, 3, 1)
        active = not back_enabled
        self.first_no_entry.set_sensitive(active)

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
        self.browse_logo_button.connect("clicked", self.on_logo_clicked)
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
        self.browse_pdf_button.connect("clicked", self.on_pdf_clicked)
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

        self.back_button = Gtk.Button("Avbryt")
        self.back_button.set_margin_right(horizontal_margin*2)
        self.back_button.set_margin_top(vert_spacer)
        self.back_button.set_margin_bottom(vertical_margin)
        grid.attach(self.back_button, 8, row, 1, 1)
        self.back_button.set_sensitive(back_enabled)

        
        # creating and attaching signal to go home
        if back_enabled:
            signaling.new("home-clicked", self) # signal to get back
        self.back_button.connect("clicked", self.on_back_clicked)


        self.load_data() # fill fields



    def on_save_clicked(self, *args):
        from norskfaktura.config import config, write_config
        config["firma"]["navn"] = self.name_entry.get_text()
        config["firma"]["org. nr"] = self.org_entry.get_text()
        config["firma"]["tlf"] = self.phone_entry.get_text()
        config["firma"]["epost"] = self.email_entry.get_text()
        config["firma"]["webside"] = self.website_entry.get_text()
        config["firma"]["adresse linje 1"] = self.address_entry_one.get_text()
        config["firma"]["adresse linje 2"] = self.address_entry_two.get_text()
        config["firma"]["postnr og sted"] = self.postal_entry.get_text()
        config["firma"]["kontonummer"] = self.account_entry.get_text()
        config["firma"]["første fakturanr"] = self.first_no_entry.get_text()
        config["faktura"]["betalingsfrist i dager"] = self.due_entry.get_text()
        config["miljø"]["logofil"] = self.logo_entry.get_text()
        config["miljø"]["pdfmappe"] = self.pdf_entry.get_text()
        if self.vat_checkbox.get_active():
            config["firma"]["mva-registrert"] = "true"
        else:
            config["firma"]["mva-registrert"] = "false"

        write_config()
        if self.back_enabled:
            self.emit("home-clicked", self)
        else:
            self.window.destroy()

    def on_back_clicked(self, widget):
        self.emit("home-clicked", self)

    def load_data(self):
        from norskfaktura.config import load_config

        cfg = load_config()
        self.name_entry.set_text(cfg["firma"]["navn"])
        self.org_entry.set_text(cfg["firma"]["org. nr"])
        self.phone_entry.set_text(cfg["firma"]["tlf"])
        self.email_entry.set_text(cfg["firma"]["epost"])
        self.website_entry.set_text(cfg["firma"]["webside"])
        self.address_entry_one.set_text(cfg["firma"]["adresse linje 1"])
        self.address_entry_two.set_text(cfg["firma"]["adresse linje 2"])
        self.postal_entry.set_text(cfg["firma"]["postnr og sted"])
        self.account_entry.set_text(cfg["firma"]["kontonummer"])
        self.first_no_entry.set_text(cfg["firma"]["første fakturanr"])
        self.due_entry.set_text(cfg["faktura"]["betalingsfrist i dager"])
        self.logo_entry.set_text(cfg["miljø"]["logofil"])
        self.pdf_entry.set_text(cfg["miljø"]["pdfmappe"])

        if cfg["firma"]["mva-registrert"] == "true" or cfg["firma"]["mva-registrert"] == "True":
            self.vat_checkbox.set_active(True)
        else:
            self.vat_checkbox.set_active(False)



    def on_logo_clicked(self, *args):

        dialog = Gtk.FileChooserDialog(
            title="Velg en bildefil av logoen for fakturaene", 
            parent=self.window, 
            action=Gtk.FileChooserAction.OPEN,
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )

        f = Gtk.FileFilter()
        f.set_name("PNG filer")
        f.add_mime_type("image/png")
        dialog.add_filter(f)

        f = Gtk.FileFilter()
        f.set_name("JPEG filer")
        f.add_mime_type("image/jpg")
        dialog.add_filter(f)

        f = Gtk.FileFilter()
        f.set_name("GIF filer")
        f.add_mime_type("image/gif")
        dialog.add_filter(f)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.logo_entry.set_text(dialog.get_filename())

        dialog.destroy()


    def on_pdf_clicked(self, *args):
        dialog = Gtk.FileChooserDialog(
            title="Velg en mappe hvor genererte PDFer skal legges",
            parent=self.window,
            action=Gtk.FileChooserAction.SELECT_FOLDER,
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Velg", Gtk.ResponseType.OK
        )
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.pdf_entry.set_text(dialog.get_filename())

        dialog.destroy()



