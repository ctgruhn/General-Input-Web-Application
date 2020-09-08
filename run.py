from flask import Flask, render_template, flash
from forms import RegisterForm, LoginForm, InputForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fbe722648272ca8bc3ff68521604bfa4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(20), nullable=False)    # may need to extend limit for longer names
    last_name = db.Column(db.String(20), nullable=False)     # may need to extend limit for longer names
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    hazards = db.relationship('Hazards', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.first_name}','{self.last_name}' '{self.email}')"

class Hazards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(20), nullable=False)
    task = db.Column(db.String(120), nullable=False)
    hazard = db.Column(db.String(20), nullable=False)
    info = db.Column(db.Text, nullable=False)
    date_submitted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Hazard('{self.area}', '{self.location}', '{self.task}', '{self.hazard}', '{self.date_submitted}')"

@app.route("/")
def index():
    title = "Generic Input- Home"
    return render_template("home.html",
    title = title)

@app.route("/input", methods=['GET', 'POST'])
def inputPage():
    title = "Input"
    form = InputForm()
    if form.validate_on_submit():
        flash(f'Hazard Successfully Submitted', 'success')
        return redirect(url_for('index'))
    return render_template("input.html",
                            title = title,
                            form=form)

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    title = "Sign In"
    form = RegisterForm()
    if form.email.data == 'temp@temp.com' and form.password.data == 'password':
        flash('You have been logged in!', 'success')
        return redirect(url_for('index'))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("signin.html",
                            title = title,
                            form = form)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    title = "Sign Up"
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template("signup.html",
    title = title,
    form = form)


if __name__ == '__main__':
      app.run(debug=True)