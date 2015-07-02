#!/usr/bin/env python
from flask import Flask, request, render_template, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy

from flask_wtf import Form
from wtforms import StringField, TextField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

from settings import BaseSettings


app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(BaseSettings)


class GuestbookItem(db.Model):
    """
    --------------
    ffsafdsafdsa
    aaaaaaaaaaaaaaa
    """
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(80))
    text = db.Column(db.Text)


class GuestbookItemForm(Form):
    author = StringField('title', validators=[DataRequired()])
    text = TextField('text', validators=[DataRequired()], widget=TextArea())


@app.route('/', methods=('GET', 'POST', ))
def index():
    form = GuestbookItemForm()
    items = GuestbookItem.query.all()
    if request.method == 'POST' and form.validate_on_submit():
        item = GuestbookItem(**form.data)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', items=items, form=form)


if __name__ == '__main__':
    app.run(debug=True)
