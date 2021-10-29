from flask import render_template

from app import app
from app.forms import myForm


@app.route('/')
@app.route('/mypage', methods=['GET', 'POST'])
def myPage():
    form = myForm.MyForm()
    if form.validate_on_submit():  # POST
        return render_template("result.html", result=form.rate_the_dog.data)
    else:
        return render_template("myPage.html", form=form)
