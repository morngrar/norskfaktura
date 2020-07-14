#!/bin/sh

sudo apt install gcc python3-pip gobject-introspection python3-gi libcairo-dev pkgconf python3-dev libcairo-gobject2 libgirepository1.0-dev && \
pip3 install --user norskfaktura-*.tar.gz

iconfolder=~/.local/share/icons/hicolor/scalable/apps
mkdir -p "$iconfolder"

cp norskfaktura.svg "$iconfolder"
cp norskfaktura.desktop ~/.local/share/applications

