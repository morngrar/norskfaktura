import norskfaktura.config as cfg
from norskfaktura.gui import show_main_window

def dev():
    """Run against development db"""
    from norskfaktura import common
    common.DBFILE = "test.db"
    common.ensure_db()
    show_main_window()

def install_icons():
    """Installs icon and desktop file into local directory"""
    import os
    icon_dir = os.path.expanduser("~/.local/share/icons/hicolor/scalable/apps/")
    app_dir = os.path.expanduser("~/.local/share/applications/")
    for d in [icon_dir, app_dir]:
        if not os.path.exists(d):
            os.makedirs(d)
    host_dir = os.path.dirname(os.path.abspath(__file__))
    icon_file = os.path.join(host_dir, "norskfaktura.svg")
    desktop_file = os.path.join(host_dir, "norskfaktura.desktop")

    import shutil
    shutil.copy(icon_file, os.path.join(icon_dir, "norskfaktura.svg"))
    shutil.copy(desktop_file, os.path.join(app_dir, "norskfaktura.desktop"))
    print("Done.")

def main():
    show_main_window()
