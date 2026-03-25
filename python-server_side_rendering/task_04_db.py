from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json(filepath):
    """Read and return data from a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def read_csv(filepath):
    """Read and return data from a CSV file as a list of dicts."""
    products = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id":       int(row["id"]),
                "name":     row["name"],
                "category": row["category"],
                "price":    float(row["price"])
            })
    return products


def read_sql(filepath):
    """Read and return data from a SQLite database."""
    try:
        conn = sqlite3.connect(filepath)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [{"id": row["id"], "name": row["name"],
                 "category": row["category"], "price": row["price"]}
                for row in rows]
    except sqlite3.Error as e:
        return None


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # --- Handle source ---
    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    elif source == 'sql':
        data = read_sql('products.db')
        if data is None:
            return render_template('product_display.html',
                                   error="Database error: could not fetch data.")
    else:
        return render_template('product_display.html', error="Wrong source")

    # --- Filter by id if provided ---
    if product_id:
        data = [p for p in data if p['id'] == int(product_id)]
        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
