from flask import Flask, render_template, request, redirect, session, send_file
from db import get_connection
from model import train_model, predict_attrition
import os

app = Flask(__name__)
app.secret_key = "secret123"


# ---------- LOGIN CHECK FUNCTION ----------
def check_login():
    if 'user' not in session:
        return False
    return True


# ---------- LOGIN ----------
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "admin":
            session['user'] = username
            return redirect('/')
        else:
            return "Invalid Login"

    return render_template('login.html')


# ---------- LOGOUT ----------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')


# ---------- HOME ----------
@app.route('/')
def index():
    if not check_login():
        return redirect('/login')
    return render_template('index.html')


# ---------- ADD EMPLOYEE ----------
@app.route('/add', methods=['GET','POST'])
def add_employee():
    if not check_login():
        return redirect('/login')

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        dept = request.form['department']
        salary = request.form['salary']
        exp = request.form['experience']
        perf = request.form['performance']
        attr = request.form['attrition']

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO employees (name, age, department, salary, experience, performance, attrition) VALUES (?,?,?,?,?,?,?)",
            (name, age, dept, salary, exp, perf, attr)
        )
        conn.commit()
        conn.close()

        return redirect('/employees')

    return render_template('add_employee.html')


# ---------- VIEW EMPLOYEES + SEARCH ----------
@app.route('/employees')
def employees():
    if not check_login():
        return redirect('/login')

    conn = get_connection()
    cursor = conn.cursor()

    search = request.args.get('search')

    if search:
        query = "SELECT * FROM employees WHERE name LIKE ?"
        cursor.execute(query, ('%' + search + '%',))
    else:
        cursor.execute("SELECT * FROM employees")

    data = cursor.fetchall()
    conn.close()

    return render_template('employees.html', employees=data)


# ---------- TRAIN MODEL ----------
@app.route('/train')
def train():
    if not check_login():
        return redirect('/login')

    msg = train_model()
    return msg


# ---------- PREDICT ----------
@app.route('/predict', methods=['GET','POST'])
def predict():
    if not check_login():
        return redirect('/login')

    if request.method == 'POST':
        age = int(request.form['age'])
        salary = float(request.form['salary'])
        experience = int(request.form['experience'])
        performance = int(request.form['performance'])

        result = predict_attrition(age, salary, experience, performance)

        if result == 1:
            prediction = "Employee may leave"
        else:
            prediction = "Employee will stay"

        return render_template('predict.html', prediction=prediction)

    return render_template('predict.html')


# ---------- DASHBOARD ----------
@app.route('/dashboard')
def dashboard():
    if not check_login():
        return redirect('/login')

    import pandas as pd
    import matplotlib.pyplot as plt

    conn = get_connection()
    df = pd.read_sql("SELECT department, salary, attrition FROM employees", conn)

    if not os.path.exists('static'):
        os.makedirs('static')

    plt.figure()
    df.groupby('department')['salary'].mean().plot(kind='bar')
    plt.title("Average Salary by Department")
    plt.savefig('static/chart1.png')
    plt.close()

    plt.figure()
    df['attrition'].value_counts().plot(kind='bar')
    plt.title("Attrition Count")
    plt.savefig('static/chart2.png')
    plt.close()

    return render_template('dashboard.html')


# ---------- DELETE ----------
@app.route('/delete/<int:id>')
def delete_employee(id):
    if not check_login():
        return redirect('/login')

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/employees')


# ---------- UPDATE ----------
@app.route('/update/<int:id>', methods=['GET','POST'])
def update_employee(id):
    if not check_login():
        return redirect('/login')

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        dept = request.form['department']
        salary = request.form['salary']
        exp = request.form['experience']
        perf = request.form['performance']
        attr = request.form['attrition']

        cursor.execute("""
            UPDATE employees 
            SET name=?, age=?, department=?, salary=?, experience=?, performance=?, attrition=?
            WHERE id=?
        """, (name, age, dept, salary, exp, perf, attr, id))

        conn.commit()
        conn.close()
        return redirect('/employees')

    cursor.execute("SELECT * FROM employees WHERE id=?", (id,))
    emp = cursor.fetchone()
    conn.close()

    return render_template('update_employee.html', emp=emp)


# ---------- DOWNLOAD REPORT ----------
@app.route('/report')
def download_report():
    if not check_login():
        return redirect('/login')

    import pandas as pd
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM employees", conn)
    df.to_csv("employees_report.csv", index=False)

    return send_file("employees_report.csv", as_attachment=True)


# ---------- IMPORTANT FOR DEPLOY ----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
