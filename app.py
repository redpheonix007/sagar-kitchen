from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)
CSV_FILE = 'log_data.csv'

# Create CSV with headers if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "Date", "Customer Name", "Brand", "Type",
            "Quantity Purchased", "Quantity Returned",
            "Delivery Address", "Delivery Man"
        ])

@app.route('/')
def index():
    return render_template('form.html', form_data={})

@app.route('/submit', methods=['POST'])
def submit():
    form_data = {
        "date": request.form['date'],
        "customer_name": request.form['customer_name'],
        "brand": request.form['brand'],
        "type": request.form['type'],
        "quantity_purchased": request.form['quantity_purchased'],
        "quantity_returned": request.form['quantity_returned'],
        "address": request.form['address'],
        "delivery_man": request.form['delivery_man']
    }

    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(form_data.values())

    retained = {
        "date": form_data['date'],
        "quantity_purchased": form_data['quantity_purchased'],
        "quantity_returned": form_data['quantity_returned']
    }

    return render_template('form.html', form_data=retained)

if __name__ == '__main__':
    app.run(debug=True)
