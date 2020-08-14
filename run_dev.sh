#!/bin/sh

pip uninstall norskfaktura
python setup.py sdist
pip install dist/*
nf-dev

