""" cmd.py

Contains functions that turns into scripts for the user if the
app is installed via pip.
"""

import norskfaktura.config as cfg
from norskfaktura.gui import show_main_window
from norskfaktura.common import HOST_DIR

def dev():
    """Run against development db"""
    from norskfaktura import common
    common.DBFILE = "test.db"
    cfg.config_file = "test.conf"
    cfg.load_config()
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
    asset_dir = os.path.join(HOST_DIR, "assets")
    icon_file = os.path.join(asset_dir, "norskfaktura.svg")
    desktop_file = os.path.join(asset_dir, "norskfaktura.desktop")

    import shutil
    shutil.copy(icon_file, os.path.join(icon_dir, "norskfaktura.svg"))
    shutil.copy(desktop_file, os.path.join(app_dir, "norskfaktura.desktop"))
    print("Done.")

def main():
    cfg.load_config()
    show_main_window()
