from flask import flash, redirect, url_for, render_template

from octo_potato import app, db
from octo_potato.forms import HelloForm
from octo_potato.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message hav been sent to the world!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)
