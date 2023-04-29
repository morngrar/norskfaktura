#!/bin/env python3

import sqlite3

def load_sql_file(dumpfile, dbfile):
    con = sqlite3.connect(dbfile)
    sql = None
    with open(dumpfile,'r') as f:
        sql = f.read()
    cur = con.cursor()
    cur.executescript(sql)
    con.close()
