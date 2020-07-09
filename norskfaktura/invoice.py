
from datetime import date, timedelta
from norskfaktura.customer import Customer

# invoice flags
PAID = 2**0
POSTED = 2**1
CREDIT_NOTE = 2**2
CANCELLED = 2**3

class Invoice:
    def __init__(self, customer):
        self.id = None
        self.customer = customer

        self.delivery_date = None
        self.delivery_address = self.customer.address_lines
        
        self.date = date.today()
        self.due = None

        self.message = None

        self.flags = 0  # no bits set

        self.rows = []  # list of lists

        # summations
        self.total_vat = 0
        self.total = 0