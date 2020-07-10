
import sqlite3
from datetime import date, timedelta

from norskfaktura.customer import Customer
from norskfaktura import common

# invoice flags
PAID = 2**0
POSTED = 2**1
CREDIT_NOTE = 2**2
CANCELLED = 2**3

class Invoice:
    def __init__(self, customer):
        self.id = None
        self.customer = customer

        self.delivery_date = date.today().strftime("%d.%m.%Y")
        self.delivery_address = self.customer.address_lines
        
        self.date = date.today()
        self.due = None

        self.message = None

        self.flags = 0  # no bits set

        self.rows = []  # list of lists

        # summations
        self.total_vat = 0
        self.total = 0

    def set_due_date(self, days_from_now):
        self.due = self.date + timedelta(days=days_from_now)

    def get_totals(self):
        return common.money_to_str(self.total_vat), common.money_to_str(self.total)

    def calculate_sums(self):
        """Recalculates the total VAT and sum"""
        vats = [int(row[1]*row[2]*row[3]*(row[4]-1)) for row in self.rows]
        totals = [row[-1] for row in self.rows]
        self.total = sum(totals)
        self.total_vat = sum(vats)

    def add_row(self, row):
        """Converts and adds row, returning properly formatted list for gui

        Also updates the summations
        """

        tmp = [
            row[0],
            common.str_to_money(row[1]),
            int(row[2]),
            1-float(row[3])/100,
            1+float(row[4])/100,
        ]
        tmp.append(int(tmp[1]*tmp[2]*tmp[3]*tmp[4]))

        self.rows.append(tmp)
        self.calculate_sums()

        discount = int(100-tmp[3]*100)
        if discount == 100:
            discount = 0

        return [
            len(self.rows),
            tmp[0], 
            common.money_to_str(tmp[1]), 
            str(row[2]), 
            str(discount), 
            str(int((tmp[4]-1)*100)),
            common.money_to_str(tmp[5])
        ]

    def get_gui_rows(self):
        tmp = []
        for i in range(len(self.rows)):
            row = self.rows[i]
            discount = int(100-row[3]*100)
            if discount == 100:
                discount = 0

            tmp.append(
                [
                    i+1,
                    row[0], 
                    common.money_to_str(row[1]), 
                    str(row[2]), 
                    str(discount), 
                    str(int((row[4]-1)*100)),
                    common.money_to_str(row[5])
                ]
            )
        return tmp

    def remove_row(self, index):
        del self.rows[index]
        self.calculate_sums()


    def post(self):
        """Sets the posted flag, and saves to db"""
        self.flags |= POSTED
        self.save()

    def save(self):
        conn = sqlite3.connect(common.DBFILE)
        c = conn.cursor()

        if self.id == None:
            c.execute(
                """
                INSERT INTO invoices (
                    customer, 
                    message, 
                    date,
                    due,
                    delivery_date,
                    delivery_address_one,
                    delivery_address_two,
                    delivery_postal_code,
                    flags)
                VALUES (?""" + ", ?"*8 + ")",
                (
                    self.customer.id,
                    self.message,
                    self.date.isoformat(),
                    self.due.isoformat(),
                    self.delivery_date,
                    self.delivery_address[0],
                    self.delivery_address[1],
                    self.delivery_address[2],
                    self.flags
                )
            )
            self.id = c.lastrowid
        else:
            c.execute(
                """
                UPDATE invoices
                SET customer = ?,
                    message = ?,
                    date = ?,
                    due = ?,
                    delivery_date = ?,
                    delivery_address_one = ?,
                    delivery_address_two = ?,
                    delivery_postal_code = ?,
                    flags = ?
                WHERE id = ?
                """,
                (
                    self.customer.id,
                    self.message,
                    self.date.isoformat(),
                    self.due.isoformat(),
                    self.delivery_date,
                    self.delivery_address[0],
                    self.delivery_address[1],
                    self.delivery_address[2],
                    self.flags,
                    self.id
                )
            )

        conn.commit()
        conn.close()
        