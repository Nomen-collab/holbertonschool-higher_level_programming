# task_02_logic.py
from flask import Flask, render_template
import json
import os # Useful for path handling, though 'items.json' in root is simple enough

app = Flask(__name__)

# --- Existing routes from previous exercise (task_01_jinja.py) ---
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
# --- End of existing routes ---


@app.route('/items')
def items_list():
    """
    Reads a list of items from items.json and renders them in items.html.
    Handles cases where the file is not found or JSON is invalid.
    """
    items_data = [] # Default to an empty list in case of errors

    # Construct the full path to items.json
    # This is more robust as it finds the file relative to the app's root path
    json_file_path = os.path.join(app.root_path, 'items.json')

    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
            # Safely get the 'items' list from the loaded data, default to empty list if key is missing
            items_data = data.get('items', [])
    except FileNotFoundError:
        # Log a warning if the file isn't found, but allow the page to render with an empty list
        print(f"Warning: {json_file_path} not found. Displaying empty list.")
        items_data = [] # Ensure it's an empty list if file not found
    except json.JSONDecodeError:
        # Log a warning if the JSON is malformed, and display an empty list
        print(f"Warning: Error decoding {json_file_path}. Ensure it's valid JSON. Displaying empty list.")
        items_data = [] # Ensure it's an empty list if JSON is invalid
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}. Displaying empty list.")
        items_data = []

    # Pass the retrieved list of items to the Jinja template
    return render_template('items.html', items=items_data)

if __name__ == '__main__':
    # Run the Flask application on port 5000 in debug mode
    # Debug mode allows for automatic server reloading on code changes
    app.run(debug=True, port=5000)
