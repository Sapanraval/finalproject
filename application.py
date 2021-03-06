from flask import Flask, abort, redirect, render_template, request, flash, url_for
import smtplib
from form import ContactForm
from flask_mail import Mail, Message
from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError
import os

## You need to install flaks_mail and flask_wtf


mail = Mail()

app = Flask(__name__)

# Sending email to my gmail account when user submit information in contact form
app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'sapanravalcs50@gmail.com'
app.config["MAIL_PASSWORD"] = 'spring2019$'

mail.init_app(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/experience")
def experience():
    return render_template('experience.html')

@app.route("/education")
def education():
    return render_template('education.html')

@app.route("/certification")
def certification():
    return render_template('certification.html')

@app.route("/skills")
def skills():
    return render_template('skills.html')

@app.route('/form', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            msg = Message(form.subject.data, sender='contact@example.com', recipients=['sapanravalcs50@gmail.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            # Display flash message once email received.
            flash(f'Thank you for your message {form.name.data}! I will reach out to you soon', 'success')
            return redirect(url_for('index'))
    return render_template('form.html',form=form)

if __name__ == '__main__':
  app.run(debug=True)
