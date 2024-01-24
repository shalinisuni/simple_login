from flask import Flask, render_template, request, redirect, url_for, flash, session
import pyodbc
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'demoapp'

# Define your Azure SQL connection parameters
server = 'solutionkraft.database.windows.net'
database = 'demosqlpro'
username = 'solutionkraft'
password = '{Solnkraft24}'
driver = '{ODBC Driver 18 for SQL Server}'
connectionString = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(connectionString)
cursor = conn.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # hashed_password = hashlib.md5(password.encode()).hexdigest()

        # Execute SQL query to check login credentials
        cursor.execute("SELECT user_id FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()

        if user:
            session['user_id'] = user.user_id
            flash('Login successful', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'error')
            return render_template('index.html')

    return render_template('index.html', msg='Invalid email or password')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return f'Welcome to the Dashboard, user #{session["user_id"]}!'
    else:
        flash('You need to log in first', 'error')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
