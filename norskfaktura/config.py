import configparser
import os

config = configparser.ConfigParser()
config_file = os.path.expanduser("~/.config/norskfaktura/norskfaktura.conf")

def ensure_config_dir():
    directory = os.path.dirname(config_file)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

def create_config():
    config['firma'] = {
        'navn' : '',
        'org. nr' : '',
        'tlf' : '',
        'epost' : '',
        'webside' : '',
        'adresse linje 1' : '',
        'adresse linje 2' : '',
        'postnr og sted' : '',
        'kontonummer' : '',
        'mva-registrert' : 'false',
        'første fakturanr' : '1',
    }

    config['faktura'] = {
        'betalingsfrist i dager' : '14'
    }

    config['miljø'] = {
        'logofil' : '',
        'pdfmappe' : ''
    }

    ensure_config_dir()

    with open(config_file, "w") as f:
        config.write(f)

def load_config():
    if not os.path.exists(config_file):
        ensure_config_dir()
        create_config()
        os.system(f"gedit {config_file}")
    else:
        config.read(config_file)

    return config


if __name__ == "__main__":
    print(load_config()["firma"].getboolean('mva-registrert'))
