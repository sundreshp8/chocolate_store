import sqlite3

def add_seasonal_flavor(name, description, available_from, available_until):
    with sqlite3.connect('chocolate_store.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO seasonal_flavors (name, description, available_from, available_until) VALUES (?, ?, ?, ?)",
            (name, description, available_from, available_until)
        )
        conn.commit()
        print(f"Seasonal flavor '{name}' added successfully.")

if __name__ == "__main__":
    # Example usage: Add a new seasonal flavor
    add_seasonal_flavor("Dark Chocolate Orange", "A rich blend of dark chocolate with a hint of orange.", "2024-11-01", "2024-12-31")
