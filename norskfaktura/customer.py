
import sqlite3

from norskfaktura import common

class Customer:
    def __init__(self):
        self.id = None
        self.name = None
        self.org_no = None
        self.address_lines = [
            "",
            "",
            "",     # postal code and place
        ]


        # Currently exists in schema, but not added to gui:
        self.tlf = None
        self.email = None
        self.discount = None

    def save(self):
        conn = sqlite3.connect(common.DBFILE)
        c = conn.cursor()

        if self.id == None:
            c.execute(
                """
                INSERT INTO customers (
                    name, 
                    org_no, 
                    address_one,
                    address_two,
                    postal_code)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    self.name,
                    self.org_no,
                    self.address_lines[0],
                    self.address_lines[1],
                    self.address_lines[2],
                )
            )
            self.id = c.lastrowid
        else:
            c.execute(
                """
                UPDATE customers
                SET name = ?,
                    org_no = ?,
                    address_one = ?,
                    address_two = ?,
                    postal_code = ?
                WHERE id = ?
                """,
                (
                    self.name,
                    self.org_no,
                    self.address_lines[0],
                    self.address_lines[1],
                    self.address_lines[2],
                    self.id
                )
            )

        conn.commit()
        conn.close()
