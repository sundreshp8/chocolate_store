import sqlite3

def create_database():
    conn = sqlite3.connect('chocolate_store.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal_flavors (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        available_from DATE,
        available_until DATE
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredient_inventory (
        id INTEGER PRIMARY KEY,
        name TEXT,
        quantity INTEGER,
        unit TEXT,
        expiration_date DATE
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS customer_feedback (
        id INTEGER PRIMARY KEY,
        suggestion TEXT,
        allergy_concern TEXT
    )''')

    conn.commit()
    conn.close()
    print("Database and tables created successfully.")

if __name__ == "__main__":
    create_database()
