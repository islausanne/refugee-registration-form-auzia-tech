from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Load existing data if file exists, otherwise start with empty list
if os.path.exists('registrations.json'):
    with open('registrations.json', 'r') as file:
        data = json.load(file)
else:
    data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('Name')
    country = request.form.get('Country')
    age = request.form.get('Age')
    number = request.form.get('Number')
    email = request.form.get('Email')

    # Save all fields
    data.append({
        'name': name,
        'country': country,
        'age': age,
        'number': number,
        'email': email
    })

    # Write back to JSON file
    with open('registrations.json', 'w') as file:
        json.dump(data, file, indent=2)

    flash('Registration submitted successfully!')
    return redirect(url_for('index'))

@app.route('/view')
def view_registrations():
    if os.path.exists('registrations.json'):
        with open('registrations.json', 'r') as file:
            registrations = json.load(file)
    else:
        registrations = []
    return render_template('view.html', registrations=registrations)

if __name__ == '__main__':
    app.run(debug=True)