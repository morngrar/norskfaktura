#!/bin/sh

pip uninstall norskfaktura
python setup.py sdist
pip install --user dist/*
nf-dev

