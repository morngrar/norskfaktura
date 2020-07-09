


import os

DBFILE = "test.db"

# Production:
# DBFILE = os.expanduser("~/.config/norskfaktura/norskfaktura.db")

from norskfaktura import load_sql_file

if not os.path.exists(DBFILE):
    host_dir = os.path.dirname(os.path.abspath(__file__))
    sql_file = os.path.join(host_dir, "schema.sql")
    load_sql_file(sql_file, DBFILE)