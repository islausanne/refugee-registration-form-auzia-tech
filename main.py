from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    country = request.form['country']
    age = request.form['age']
    number = request.form['number']
    email = request.form['email']


    data.append({'name': name, 'country': country, 'age': age})


    with open('registrations.json', 'w') as file:
        json.dump(data, file, indent=2)

    # TODO: Save form data to a JSON file (worksheet Part 1)

    flash('Registration submitted successfully!')
    return redirect(url_for('index'))


@app.route('/view')
def view_registrations():
    # TODO: Read data from registrations.json and send to template (worksheet Part 2)
    @app.route('/view')
    def view_registrations():
        with open('registrations.json', 'r') as file:
            data = json.load(file)
        return render_template('view.html', registrations=data)

if __name__ == '__main__':
    app.run(debug=True)
hello
