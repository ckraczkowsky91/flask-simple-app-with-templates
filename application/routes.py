from flask import render_template
from main import app

@app.route('/')
def firstPage():
    return render_template('part-one.html')

@app.route('/punchline')
def secondPage():
    return render_template('part-two.html')
