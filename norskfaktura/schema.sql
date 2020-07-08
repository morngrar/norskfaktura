CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address_one TEXT NOT NULL,
    address_two TEXT,
    postal_code TEXT NOT NULL,
    org_no TEXT,
    tlf TEXT,
    email TEXT
);

CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY,
    customer INTEGER, -- FK
    description TEXT,
    date INTEGER NOT NULL,
    due INTEGER NOT NULL,
    delivery_date TEXT,
    delivery_address_one TEXT,
    delivery_address_two TEXT,
    delivery_postal_code TEXT,

    -- boolean flags 1/0 (sqlite has no 'boolean')
    posted INTEGER NOT NULL,
    paid INTEGER NOT NULL,
    cancelled INTEGER NOT NULL,
    credit_note INTEGER NOT NULL,

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
    vat REAL NOT NULL, -- percentage factor
    FOREIGN KEY (invoice)
        REFERENCES invoices (id)
            ON DELETE CASCADE
);

-- Most recent ID in table:
-- SELECT id
-- FROM table
-- WHERE id = (SELECT MAX(id) FROM table)
