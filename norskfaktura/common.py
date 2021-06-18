
""" common.py

Contains common functionality across the app. Utility functions and globals.
"""

import os

HOST_DIR = os.path.dirname(os.path.abspath(__file__))

# Production:
DBFILE = os.path.expanduser("~/.config/norskfaktura/norskfaktura.db")

from norskfaktura import load_sql_file
from norskfaktura.config import ensure_config_dir

def ensure_db():
    ensure_config_dir()
    if not os.path.exists(DBFILE):
        sql_file = os.path.join(HOST_DIR, "schema.sql")
        load_sql_file(sql_file, DBFILE)

ensure_db()

# For file naming and date formatting:
def pad_zeroes(n, padding): 
    """Returns string from number n, padded to lengt with leading zeroes"""
    if n == 0 and padding-1 == 0:
        return "0"
    elif n - 10**(padding-1) >= 0: 
        return str(n) 
    else: 
        return f"0{pad_zeroes(n, padding-1)}" 


def str_to_money(string):
    """Takes a number, with or without a decimal point, and converts it to money"""
    string = string.replace(",",".")
    return int(round(float(string)*100))


def money_to_str(integer):
    """Takes an integer containing full money value with cents and returns string"""
    return f"{int(integer/100)},{pad_zeroes(integer%100, 2)}"