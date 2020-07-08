import configparser
import os

config = configparser.ConfigParser()
config_file = os.path.join(
    os.path.expanduser("~"), 
    ".config/norskfaktura/config.conf"
)

def ensure_config_dir():
    directory = os.path.dirname(config_file)
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_config():
    config['firma'] = {
        'navn' : '',
        'org. nr' : '',
        'tlf' : '',
        'webside' : '',
        'adresse linje 1' : '',
        'adresse linje 2' : '',
        'postnr og sted' : '',
        'kontonummer' : '',
        'mva-registrert' : 'false',
        'første fakturanr' : '1',
    }

    config['miljø'] = {
        'pdf-kommando' : 'evince',
    }

    ensure_config_dir()

    with open(config_file, "w") as f:
        config.write(f)

def load_config():
    if not os.path.exists(config_file):
        create_config()
    else:
        config.read(config_file)

    return config


if __name__ == "__main__":
    print(load_config()["firma"].getboolean('mva-registrert'))