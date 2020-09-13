from flask import render_template, url_for, flash, redirect
from hazardapp import app, db
from hazardapp.forms import RegisterForm, LoginForm, InputForm
from hazardapp.models import User, Hazards

@app.route("/")
@app.route("/home")
def index():
    title = "Generic Input- Home"
    return render_template("home.html",
    title = title)

@app.route("/input", methods=['GET', 'POST'])
# @login_required
def input_hazard():
    title = "Input"
    form = InputForm()
    if form.validate_on_submit():
        flash(f'Hazard Successfully Submitted', 'success')
        return redirect(url_for('index'))
    return render_template("input.html",
                            title = title,
                            form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    title = "Sign Up"
    form = RegisterForm()
    if form.email.data == 'temp@temp.com' and form.password.data == 'password':
        flash('You have been logged in!', 'success')
        return redirect(url_for('index'))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("register.html",
                            title = title,
                            form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    title = "Log In"
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template("login.html",
            title = title,
            form = form)