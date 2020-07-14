# Norsk faktura

## Hvordan kjøre tester

    python3 setup.py test

## Lage og bruke et virtuelt miljø for utvikling:
Lager et virtuelt mmiljø under mappen 'env':

    python -m venv env

Aktivere det virtuelle miljøet:

    source env/bin/activate

Deaktivere det virtuelle miljøet:

    deactivate


## pakker som må installeres for virtuelt miljø skal fungere

Kjør denne kommandoen på fedora:

    sudo dnf install gcc gobject-introspection gobject-introspection-devel cairo cairo-devel pkgconf-pkg-config python3-devel cairo-gobject-devel

Kjør denne kommandoen på ubuntu 18.04:

    sudo apt install gcc python3-pip gobject-introspection python3-gi libcairo-dev pkgconf python3-dev libcairo-gobject2 libgirepository1.0-dev

ref: [https://stackoverflow.com/a/54795222](https://stackoverflow.com/a/54795222)