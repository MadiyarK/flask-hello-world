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