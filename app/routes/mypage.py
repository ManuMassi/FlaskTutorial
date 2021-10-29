from flask import render_template

from app import app
from app.forms import myForm


@app.route('/')
@app.route('/mypage', methods=['GET', 'POST'])
def myPage():
    form = myForm.MyForm()
    if form.validate_on_submit():  # POST
        result = form.rate_the_dog.data
        name = form.dog_name.data
        good_boy = False
        if result == "Good boy":
            good_boy = True
        return render_template("result.html", result=result, good_boy=good_boy, name=name)
    else:
        return render_template("myPage.html", form=form)
