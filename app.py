import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        # Check if username already exists
        already_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
            )
        
        if already_exists:
            flash('Username already in use')
            return redirect(url_for("registration"))

        registration = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(registration)

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("registration.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username exists in database
        # Python uses the name attribute from the form inputs
        # So username below refers to the name attribute of 
        # the username input field
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Check input password against the hashed password
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # If passwords do not match
                flash("Incorrect username/password entered, please try again")
                return redirect(url_for("login"))
        
        else:
            # Username not in database
            flash("Incorrect username/password entered, please try again")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/albums")
def albums():
    albums = list(mongo.db.albums.find())
    genres = list(mongo.db.genres.find())
    return render_template("albums.html", albums=albums, genres=genres)


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You are now logged out")
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
