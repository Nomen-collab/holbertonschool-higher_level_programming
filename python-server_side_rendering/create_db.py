# create_db.py
import sqlite3
import os

def create_database():
    """
    Creates the products.db SQLite database and populates it with initial data.
    """
    db_path = 'products.db'

    # Remove existing database file if it exists to ensure a clean start
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Removed existing {db_path}")

    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create Products table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')

        # Insert initial data
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99),
            (3, 'Desk Chair', 'Furniture', 120.00),
            (4, 'Mechanical Keyboard', 'Electronics', 99.50),
            (5, 'Webcam', 'Electronics', 49.99)
        ''')

        conn.commit()
        print(f"Database {db_path} created and populated successfully.")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_database()
