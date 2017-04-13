from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/barres')
def barres():
    return render_template('barres.html')
