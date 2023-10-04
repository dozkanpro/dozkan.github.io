from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import smtplib
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
Bootstrap5(app)

OWN_EMAIL = os.environ.get('OWN_EMAIL')
OWN_PASSWORD = os.environ.get('OWN_PASSWORD')


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email Adress', validators=[DataRequired(), Length(min=6, max=35)])
    phone_number = StringField('Phone Number')
    message = StringField('Message', validators=[DataRequired(), Length(min=15, max=100)])
    submit = SubmitField('Send')


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        name = contact_form.name.data
        email = contact_form.email.data
        phone = contact_form.phone_number.data
        message = contact_form.message.data
        send_email(name, email, phone, message)
        return render_template('contact.html', form=contact_form, msg_sent=True)
    return render_template("contact.html", form=contact_form, msg_sent=False)


def send_email(name, email, phone, message):
    email_msg = f"Subject: Message From Professional Portfolio\n\nName: {name}\nEmail:{email}\nPhone:{phone}\n" \
                f"message:{message}"
    email_msg = email_msg.encode('ascii', 'ignore').decode('ascii')
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, msg=email_msg)


@app.route("/articles")
def articles():
    return render_template("articles.html")


if __name__ == '__main__':
    app.run(debug=True, port=5003)
