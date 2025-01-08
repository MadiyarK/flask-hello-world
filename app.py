from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello, World! and Madiyar!'


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/Aiganym')
def aiganym():
    return render_template('Aiganym.html')


@app.route('/Mama')
def mama():
    return render_template('Mama.html')


@app.route('/Papa')
def papa():
    return render_template('Papa.html')

@app.route('/Greg')
def greg():
    return render_template('Greg.html')

@app.route('/Aari')
def arai():
    return render_template('Arai.html')