"""from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('beforeLogin.html')

@app.route('/after')
def after_login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()"""




from flask import Flask, render_template

app = Flask(__name__)

# Route for the before login page
@app.route('/')
def hello_world():  # put application's code here
    return render_template('beforeLogin.html')

# Route for the after login page
@app.route('/after')
def after_login():
    return render_template('afterLogin.html')

if __name__ == 'main':
    app.run()