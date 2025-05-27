from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure value in production

# Predefined username and password
USERNAME = 'admin'
PASSWORD = 'password123'

# Dummy product list with images, quantities, and shipping address
PRODUCTS = [
    {
        'id': 1,
        'name': 'Laptop',
        'price': 1000,
        'image': 'laptop.jpg',
        'description': 'A high-performance laptop for work and play.',
        'quantity': 5,
        'shipping_address': '123 Main St, Big City, Country'
    },
    {
        'id': 2,
        'name': 'Smartphone',
        'price': 500,
        'image': 'smartphone.jpg',
        'description': 'A sleek smartphone with the latest features.',
        'quantity': 10,
        'shipping_address': '456 Oak Ave, Small Town, Country'
    },
    {
        'id': 3,
        'name': 'Tablet',
        'price': 300,
        'image': 'tablet.jpg',
        'description': 'A lightweight tablet for entertainment and productivity.',
        'quantity': 7,
        'shipping_address': '789 Pine Rd, Capital City, Country'
    },
]

def get_product(product_id):
    return next((p for p in PRODUCTS if p['id'] == product_id), None)

@app.route('/')
def index():
    if 'username' in session:
        return render_template('products.html', products=PRODUCTS)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['username'] = username
            return redirect(url_for('index'))
        flash('Invalid credentials. Please try again.')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    product = get_product(product_id)
    if not product:
        return "Product not found", 404
    return render_template('product_detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)