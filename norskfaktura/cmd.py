import norskfaktura.config as cfg
from norskfaktura.gui import show_main_window

def test():
    print(cfg.load_config()["firma"].getboolean('mva-registrert'))
    show_main_window()