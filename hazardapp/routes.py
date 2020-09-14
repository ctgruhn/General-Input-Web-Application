from flask import render_template, url_for, flash, redirect, request
from hazardapp import app, db, bcrypt
from hazardapp.forms import RegisterForm, LoginForm, InputForm
from hazardapp.config import AREA_LIST, HAZARD_LIST
from hazardapp.models import User, Hazards
from flask_login import login_user, logout_user, current_user, login_required

@app.route("/")
@app.route("/home")
@login_required
def index():
    title = "Generic Input- Home"
    hazards = Hazards.query.all()
    return render_template("home.html",
                            title = title,
                            AREA_LIST=AREA_LIST,
                            HAZARD_LIST=HAZARD_LIST,
                            hazards=hazards)

@app.route("/input", methods=['GET', 'POST'])
@login_required
def input_hazard():
    title = "Input"
    form = InputForm()
    if form.validate_on_submit():
        hazard = Hazards(area=form.area.data,
                        location=form.location.data,
                        task=form.task.data,
                        hazard=form.hazard.data,
                        details=form.details.data,
                        date_submitted=form.date.data,
                        user_id=current_user.id)
        db.session.add(hazard)
        db.session.commit()
        flash(f'Hazard Successfully Submitted', 'success')
        return redirect(url_for('index'))
    return render_template("input.html",
                            title = title,
                            form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = "Sign Up"
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Account Successfully Created!", 'success')
        return redirect(url_for('index'))
    return render_template("register.html",
                            title = title,
                            form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = "Log In"
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template("login.html",
            title = title,
            form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/account")
@login_required
def account():
    title = "Account"
    return render_template("account.html", title = title)