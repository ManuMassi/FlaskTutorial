from flask import render_template

from app import app


@app.route('/')
@app.route('/result/<string:result>')
def index(result):
    return render_template("result.html", result=result)
