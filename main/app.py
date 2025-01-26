from flask import Flask, render_template, request, redirect, url_for, flash
from DataAccessLayer.Users import check_credentials_students, check_credentials_teacher

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def home():
    return render_template('beforeLogin.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if check_credentials_students(username, password):
        flash('Login successful!', 'success')
        return redirect(url_for('homepage'))
    else:
        flash('Invalid username or password. Please try again.', 'danger')
        return redirect(url_for('after_login1'))


@app.route('/loginTeacher', methods=['POST'])
def login_teacher():
    username = request.form.get('username')
    password = request.form.get('password')

    if check_credentials_teacher(username, password):
        flash('Login successful!', 'success')
        return redirect(url_for('homepage_teach'))
    else:
        flash('Invalid username or password. Please try again.', 'danger')
        return redirect(url_for('after_login'))


@app.route('/after')
def after_login():
    return render_template('loginTeacher.html')


@app.route('/after1')
def after_login1():
    return render_template('loginStudent.html')


@app.route('/homepage')
def homepage():
    return render_template('homeStudent.html')


@app.route('/homepageTeach')
def homepage_teach():
    return render_template('homeTeacher.html')


@app.route('/maths')
def math():
    return render_template('mathEdit.html')


@app.route('/sciences')
def science():
    return render_template('ScienceEdit.html')


@app.route('/english')
def english():
    return render_template('englishEdit.html')


if __name__ == '__main__':
    app.run(debug=True)
