from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql8669523:RPRTb7EiLg@sql8.freesqldatabase.com:3306/sql8669523'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
db = SQLAlchemy(app)

class createCustomer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    Gender = db.Column(db.String(20), nullable = False)
    Email = db.Column(db.String(100), nullable = False)

@app.route('/')
def index():
    message = request.args.get('message')
    all_customers = createCustomer.query.all()
    print(all_customers)
    return render_template('index.html', items = all_customers, message = message)

@app.route('/add-customer', methods=['GET', 'POST'])
def add():
    try:
        message = "Customer added Successfully!"

        if request.method == 'POST':
            name = request.form['name']
            gender = request.form['gender']
            email = request.form['email']
            new_customer = createCustomer(name=name, Gender=gender, Email=email)
            db.session.add(new_customer)
            db.session.commit()

            return redirect(url_for('index',message= message))

        return render_template('add.html')

    except Exception as e:
        return redirect(url_for('index', message=e))

@app.route('/editCustomer/<int:customer_id>', methods=['POST', 'GET'])
def editCustomer(customer_id):
    try:
        message = "Customer updated Successfully!"
        customer = createCustomer.query.get_or_404(customer_id)

        if request.method == 'POST':
            customer.name = request.form['name']
            customer.Gender = request.form['gender']
            customer.Email = request.form['email']
            db.session.commit()

            return redirect(url_for('index',message= message))

        return render_template('update.html', items = customer)

    except Exception as e:
        return redirect(url_for('index', message=e))

@app.route('/deleteCustomer/<int:customer_id>')
def deleteCustomer(customer_id):
    try:
        message = "Customer deleted successfully!"
        customer = createCustomer.query.get_or_404(customer_id)
        db.session.delete(customer)
        db.session.commit()

        return redirect(url_for('index', message = message))

    except Exception as e:
        return redirect(url_for('index', message=e))

with app.app_context():
    db.create_all()

if __name__ == "__main__":

    app.run(debug = True, port = 2000)