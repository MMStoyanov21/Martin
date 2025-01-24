from flask import Flask, render_template, request, redirect, url_for, flash
from DataAccessLayer.Users import check_credentials

app = Flask(__name__)
app.secret_key = 'your_secret_key'
@app.route('/')
def home():
    return render_template('beforeLogin.html')

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


@app.route('/login', methods=['POST'])  # New route for login
def login():
    username = request.form['username']
    password = request.form['password']

    if check_credentials(username, password):
        return redirect(url_for('homepage'))  # Redirect to homepage on success
    else:
        flash('Invalid username or password.')  # Flash an error message
        return redirect(url_for('after_login1'))
if __name__ == '__main__':
    app.run(debug=True)
