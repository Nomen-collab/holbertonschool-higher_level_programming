# task_04_db.py
from flask import Flask, render_template, request
import json
import csv
import sqlite3 # New import for SQLite
import os

app = Flask(__name__)

# --- Existing routes from previous exercises (for completeness) ---
@app.route('/')
def home():
    """
    Renders the home page (index.html).
    """
    return render_template('index.html')

@app.route('/about')
def about():
    """
    Renders the about page (about.html).
    """
    return render_template('about.html')

@app.route('/contact')
def contact():
    """
    Renders the contact page (contact.html).
    """
    return render_template('contact.html')

@app.route('/items')
def items_list():
    """
    Reads items from items.json and renders them in items.html.
    """
    items_data = []
    json_file_path = os.path.join(app.root_path, 'items.json')
    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
            items_data = data.get('items', [])
    except FileNotFoundError:
        print(f"Warning: {json_file_path} not found. Displaying empty list.")
    except json.JSONDecodeError:
        print(f"Warning: Error decoding {json_file_path}. Ensure it's valid JSON. Displaying empty list.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Displaying empty list.")
    return render_template('items.html', items=items_data)
# --- End of existing routes ---


# --- File reading functions (from task_03_files.py) ---
def read_json_products(file_path):
    """
    Reads and parses product data from a JSON file.
    Converts 'id' to int and 'price' to float.
    Returns (products_list, error_message_or_None).
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            products = []
            for item in data:
                if all(k in item for k in ["id", "name", "category", "price"]):
                    try:
                        product = {
                            'id': int(item['id']),
                            'name': item['name'],
                            'category': item['category'],
                            'price': float(item['price'])
                        }
                        products.append(product)
                    except (ValueError, TypeError) as e:
                        print(f"Warning: Skipping malformed product in JSON: {item} - {e}")
                else:
                    print(f"Warning: Skipping product with missing keys in JSON: {item}")
            return products, None
    except FileNotFoundError:
        return None, "Data file (JSON) not found."
    except json.JSONDecodeError as e:
        return None, f"Error parsing JSON data: {e}. Ensure file is valid JSON."
    except Exception as e:
        return None, f"An unexpected error occurred while reading JSON: {e}"


def read_csv_products(file_path):
    """
    Reads and parses product data from a CSV file.
    Converts 'id' to int and 'price' to float.
    Returns (products_list, error_message_or_None).
    """
    products = []
    try:
        with open(file_path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if all(col in row for col in ["id", "name", "category", "price"]):
                    try:
                        product = {
                            'id': int(row['id']),
                            'name': row['name'],
                            'category': row['category'],
                            'price': float(row['price'])
                        }
                        products.append(product)
                    except (ValueError, TypeError) as e:
                        print(f"Warning: Skipping malformed product in CSV: {row} - {e}")
                else:
                    print(f"Warning: Skipping product with missing columns in CSV: {row}")
            return products, None
    except FileNotFoundError:
        return None, "Data file (CSV) not found."
    except csv.Error as e:
        return None, f"Error parsing CSV data: {e}. Ensure file is valid CSV."
    except Exception as e:
        return None, f"An unexpected error occurred while reading CSV: {e}"
# --- End of file reading functions ---


# --- New SQLite reading function ---
def read_sql_products(db_path):
    """
    Reads product data from a SQLite database.
    Returns (products_list, error_message_or_None).
    """
    products = []
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        for row in rows:
            # Map SQL row to dictionary format expected by template
            product = {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            }
            products.append(product)
        return products, None
    except sqlite3.Error as e:
        return None, f"Database error: {e}. Ensure products.db exists and table 'Products' is correct."
    except Exception as e:
        return None, f"An unexpected error occurred while reading from DB: {e}"
    finally:
        if conn:
            conn.close()
# --- End of new SQLite reading function ---


@app.route('/products')
def product_display():
    """
    Displays product data from JSON, CSV, or SQLite based on 'source' query parameter.
    Filters by 'id' if provided.
    """
    source = request.args.get('source')
    product_id_param = request.args.get('id')

    products = []
    error_message = None

    db_path = os.path.join(app.root_path, 'products.db')

    if source == 'json':
        file_path = os.path.join(app.root_path, 'products.json')
        products, error_message = read_json_products(file_path)
    elif source == 'csv':
        file_path = os.path.join(app.root_path, 'products.csv')
        products, error_message = read_csv_products(file_path)
    elif source == 'sql': # New source handling
        products, error_message = read_sql_products(db_path)
    else:
        # Invalid source parameter
        error_message = "Wrong source. Please specify 'source=json', 'source=csv', or 'source=sql'."
        products = []

    # If data was successfully loaded (products is not None and no file/DB reading error)
    if products is not None and not error_message:
        if product_id_param:
            try:
                product_id_int = int(product_id_param)
                filtered_products = [p for p in products if p['id'] == product_id_int]
                if not filtered_products:
                    error_message = "Product not found."
                products = filtered_products
            except ValueError:
                error_message = "Invalid product ID. Must be an integer."
                products = []
    elif products is None: # This means a file/DB reading error occurred (error_message already set)
        products = []

    return render_template('product_display.html', products=products, error_message=error_message)


if __name__ == '__main__':
    # Run the Flask application on port 5000 in debug mode
    app.run(debug=True, port=5000)
