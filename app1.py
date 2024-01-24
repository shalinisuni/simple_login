from flask import Flask, render_template, redirect, session, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://solutionkraft:Solnkraft24@solutionkraft.database.windows.net/demosqlpro?driver=ODBC+Driver+18+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'demoapp'

# Create SQLAlchemy object
db = SQLAlchemy(app)

# Create Flask-Mail object
mail = Mail(app)

# Create URLSafeTimedSerializer object
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Define User model
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50))
    mobile = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))

class Transaction(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    target_name = db.Column(db.String(50))
    count = db.Column(db.Integer)
    date = db.Column(db.DateTime, server_default=db.func.now())

class Target(db.Model):
    target_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    target_name = db.Column(db.String(50))
    total_target_count = db.Column(db.Integer)
    cumulative_target = db.Column(db.Integer)

# Routes

@app.route('/logout')
def logout():
    session.pop('email', None)
    return render_template('index.html')

@app.route('/cancel')
def cancel():
    session.pop('email', None)
    return render_template('index.html')

@app.route('/')
def home():
    return render_template("index.html")

@app.before_request
def before_request():
    session.permanent = True
    session.modified = True 

@app.route('/login', methods=['POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        password = generate_password_hash(password)
        user = user.query.filter_by(email=email, password=password).first()
        if User:
            session['user_id'] = User.user_id
            return redirect(url_for('target_page'))
        else:
            flash("Invalid email or password", 'error')
            return render_template('index.html')
    return render_template('index.html', msg='Invalid email or password')

def get_target_data(user_id, target_name):
    target = Target.query.filter_by(user_id=user_id, target_name=target_name).first()
    return target.total_target_count, target.cumulative_target

# ... Other routes ...

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
