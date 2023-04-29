CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address_one TEXT NOT NULL,
    address_two TEXT,
    postal_code TEXT NOT NULL,
    org_no TEXT,
    tlf TEXT,
    discount INTEGER,
    email TEXT
);

CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY,
    customer INTEGER, -- FK
    message TEXT,
    date TEXT NOT NULL, -- ISO format
    due TEXT NOT NULL, -- ISO format
    delivery_date TEXT,
    delivery_address_one TEXT,
    delivery_address_two TEXT,
    delivery_postal_code TEXT,

    credit_ref INTEGER,  -- reference in case of a credit note, may be NULL

    customer_balance INTEGER,    -- amount already paid by customer

    -- boolean flags set as bits (bitwise operators as in python/c++)
    flags INTEGER NOT NULL,

    FOREIGN KEY (customer)
        REFERENCES customers (id)
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS invoice_items (
    id INTEGER PRIMARY KEY,
    invoice INTEGER, -- FK
    description TEXT NOT NULL,
    price INTEGER NOT NULL,  -- 'øre' part of integer
    amount INTEGER NOT NULL,
    discount REAL NOT NULL,  -- percentage factor
    vat REAL NOT NULL, -- percentage factor
    FOREIGN KEY (invoice)
        REFERENCES invoices (id)
            ON DELETE CASCADE
);

