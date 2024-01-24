from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__)

# Configure your Azure SQL database connection
app.config['DB_CONNECTION_STRING'] = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=solutionkraft.database.windows.net;DATABASE=demosqlpro;UID=solutionkraft;PWD=Solnkraft24;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

def connect_to_database():
    return pyodbc.connect(app.config['DB_CONNECTION_STRING'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Connect to the database
    try:
        conn = connect_to_database()
        cursor = conn.cursor()

        # Query to check user credentials
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()

        # Close the database connection
        cursor.close()
        conn.close()

        if user:
            # Authentication successful, redirect to the welcome page
            return redirect(url_for('welcome'))
        else:
            # Authentication failed, redirect back to the login page with an error message
            return render_template('index.html', error='Invalid email or password')

    except Exception as e:
        return f"Error: {e}"

@app.route('/welcome')
def welcome():
    return "Welcome Shalini"

if __name__ == '__main__':
    app.run(debug=True)
