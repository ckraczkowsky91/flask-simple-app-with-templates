from flask import render_template
from main import app

@app.route('/basic-template')
def basicTemplate():
    return render_template('basic-template.html')

@app.route('/')
@app.route('/setup')
def firstPage():
    return render_template('part-one.html')

@app.route('/punchline')
def secondPage():
    return render_template('part-two.html')
