# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)


# route decorator binds a function to a URL
@app.route('/')
def hello():
    return 'Hello world from Flask!'

@app.route('/acr')
def acr1():
    return '<p>Someone 1: YMCA - Young Men\'s Christian Association</p>' \
    '<p>Someone 2: LOL - Laugh Out Loud</p>' \
    '<p>Someone 3: FBI - Federal Bureau of Investigation</p>'


@app.route('/nico')
def nico():
    return render_template('template.html', message='Nico: DW - Don\'t Worry')