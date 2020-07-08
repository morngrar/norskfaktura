import norskfaktura.config as cfg
from norskfaktura.gui import testWindow

def test():
    print(cfg.load_config()["firma"].getboolean('mva-registrert'))
    testWindow()