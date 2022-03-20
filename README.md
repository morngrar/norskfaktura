<p align="center">
  <img src="https://raw.githubusercontent.com/morngrar/norskfaktura/master/norskfaktura/assets/norskfaktura.png">
</p>

# Norsk Faktura


Norsk Faktura er et fakturaprogram for moderne linux, laget for å tilfredsstille norske juridiske krav. Det lagrer all informasjon lokalt på maskinen.

<p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/6575679/112526840-b1139100-8da2-11eb-8a3e-4fa64f04f802.png">
</p>

<p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/6575679/112526852-b375eb00-8da2-11eb-864a-63a8ddb1eaf1.png">
</p>

## Installasjon
### Eksterne avhengigheter

Det er en del pakker som må installeres på systemet via vanlig pakkebehandling før man kan installere programmet via pip

Kjør denne kommandoen på fedora:

    sudo dnf install gcc gobject-introspection gobject-introspection-devel cairo cairo-devel pkgconf-pkg-config python3-devel cairo-gobject-devel

Kjør denne kommandoen på ubuntu 18.04:

    sudo apt install gcc python3-pip gobject-introspection python3-gi libcairo-dev pkgconf python3-dev libcairo-gobject2 libgirepository1.0-dev

ref: [https://stackoverflow.com/a/54795222](https://stackoverflow.com/a/54795222)

### Installering via pip
Når de eksterne avhengighetene er tilfredsstilt kan man installere programmet via pip:

    pip install --user norskfaktura

For ubuntu 18.04:

    pip3 install --user norskfaktura

Dette gir systemet kommandoen `norskfaktura` som kan brukes til å starte programmet via terminalen, men sannsynligvis vil man gjerne ha et menyikon man kan trykke på. Da kan man kjøre:

    nf-install-icons

og man vil etterpå (under Gnome) finne programmet blant alle andre programmer som 'Norsk Faktura'.

### Oppdatering av programmet
Man kan installere eventuelle oppdateringer også v.h.a pip:

    pip install --user norskfaktura --upgrade


### Konfigurering
Når du starter applikasjonen for første gang vil du få opp et vindu for å legge inn informasjon om ditt firma/organisasjon. Om du oppdager at du har gjort noe feil, eller vil gjøre endringer senere, kan du komme tilbake til denne skjermen ved å klikke på "instillinger"-knappen nede i høyre hjørne av hovedbildet.

Foruten første fakturanummer og filstiene til pdf-mappen og logoen, så skriver du inn resten av feltene slik du vil at de skal vises på fakturaen.


## Lage og bruke et virtuelt miljø for utvikling:
**Merk: det er per nå ikke mulig å utvikle programmet fra innsiden av et virtuelt miljø på en enkel måte, se #10**

Lager et virtuelt mmiljø under mappen 'env':

    python -m venv env

Aktivere det virtuelle miljøet:

    source env/bin/activate

Deaktivere det virtuelle miljøet:

    deactivate


### Hvordan kjøre tester

Det er enda ikke skrevet tester, men når de kommer på plass kjører man dem med denne kommandoen:

    python3 setup.py test
