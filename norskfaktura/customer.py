
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

    def address_oneliner(self):
        tmp = ""
        if self.address_lines[0]:
            tmp += self.address_lines[0] 

        if self.address_lines[1]:
            if tmp:
                tmp += " "
            tmp += self.address_lines[1]

        tmp += f", {self.address_lines[2]}"

        return tmp
        

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

def search_customers(search_string):
    search_string = f"%{search_string}%"

    conn = sqlite3.connect(common.DBFILE)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute(
        """
        SELECT *
        FROM customers
        WHERE name LIKE ?
        """,
        (search_string,)
    )

    result = c.fetchall()

    conn.commit()
    conn.close()

    customer_list = []
    for row in result:
        elem = Customer()
        elem.id = row['id']
        elem.name = row['name']
        elem.address_lines[0] = row['address_one']
        elem.address_lines[1] = row['address_two']
        elem.address_lines[2] = row['postal_code']
        elem.org_no = row['org_no']
        customer_list.append(elem)

    return customer_list

def get_customer_by_id(id):
    conn = sqlite3.connect(common.DBFILE)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute(
        """
        SELECT *
        FROM customers
        WHERE id = ?
        """,
        (id,)
    )

    result = c.fetchone()

    conn.commit()
    conn.close()

    customer = Customer()
    customer.id = result['id']
    customer.name = result['name']
    customer.address_lines[0] = result['address_one']
    customer.address_lines[1] = result['address_two']
    customer.address_lines[2] = result['postal_code']
    customer.org_no = result['org_no']

    return customer