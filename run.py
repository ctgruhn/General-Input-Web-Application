from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    title = "Generic Input- Home"
    return render_template("home.html",
    title = title)

@app.route("/input")
def inputPage():
    title = "Input"
    return render_template("input.html",
    title = title)

@app.route("/signin")
def signin():
    title = "Sign In"
    return render_template("signin.html",
    title = title)

@app.route("/signup")
def signup():
    title = "Sign Up"
    return render_template("signup.html",
    title = title)


if __name__ == '__main__':
      app.run(debug=True)