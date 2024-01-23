import pyodbc
from flask import Flask, render_template,request,session,flash
from . import app


#Database connection configuration
# server = 'solutionkraft.database.windows.net'
# database = 'demosqlpro'
# username = 'solutionkraft'
# password = '{Solnkraft24}'
# driver = '{ODBC Driver 18 for SQL Server}'
# conn_str = f'DRIVER={driver};SERVER=tcp:{server},1433;DATABASE={database};UID={username};PWD={password};Connect Timeout=30'
# conn=pyodbc.connect(conn_str)
# cursor=conn.cursor()
app.config['SECRET_KEY'] = 'demoapp'


# @app.route('/login',methods=['GET','POST'])
# def index():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         print(email,password)
#         # user_id = get_user_id(email, password)
#         user_id=1
#         print(user_id)
#         if user_id is not None:
#             session['user_id'] = user_id
#             return "Hello world"
#         else:
#             flash("Invalid email or password",'error')
#             return render_template('index.html')
       
#     return render_template('index.html', msg='Invalid email or password')

       
        
# def get_user_id(email, password):
#    cursor.execute("SELECT user_id FROM users WHERE email = ? AND password = ?",(email,password))
#    user = cursor.fetchone()
#    print(type(user))
            
#    return user[0] if user else None
        
@app.route('/')
def home():
    return render_template("index.html")