import norskfaktura.config as cfg
from norskfaktura.gui import show_main_window

def test():
    from norskfaktura import common
    common.DBFILE = "test.db"
    common.ensure_db()
    show_main_window()