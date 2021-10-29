from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    hello = "hello"
    return render_template("index.html", hello=hello)
