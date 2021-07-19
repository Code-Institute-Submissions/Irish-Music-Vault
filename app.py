import os
import time
# from time import time, ctime
from flask import (
    Flask, flash, render_template,
    redirect, request, session,
    url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

"""
Below is information for initialisiing Flask using enviornment
variables stored in the hidden env.py file
"""
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    top_rated_albums = list(mongo.db.albums.find().sort("rating", -1).limit(6))
    recently_added_albums = list(mongo.db.albums.find().sort(
        "created_at", -1).limit(6))
    return render_template(
        "home.html", recently_added_albums=recently_added_albums,
        top_rated_albums=top_rated_albums)


@app.route("/registration", methods=["GET", "POST"])
def registration():
    # Check if user is logged in, if so disallow
    # access to this page for logged out users
    if "user" in session:
        return redirect(url_for('home'))

    if request.method == "POST":
        # Check if username already exists and signal
        # the user accordingly
        already_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
            )

        if already_exists:
            flash('Username already in use')
            return redirect(url_for("registration"))

        registration = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        # Make sure email field filled out correctly
        error = None
        email = registration['email']
        if not email or '@' not in email:
            error = "Please enter a valid email address"
            return render_template("registration.html",
                                   error=error, email=email)

        mongo.db.users.insert_one(registration)

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("registration.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Check if user is logged in, if so disallow
    # access to this page for logged out users
    if "user" in session:
        return redirect(url_for('home'))

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


@app.route("/profile", methods=["GET", "POST"])
def profile():
    # if User attempts to access profile page
    # while not logged in, they will be
    # redirected to the home page
    if "user" not in session:
        return redirect(url_for('home'))

    count = mongo.db.albums.count_documents({"created_by": session["user"]})
    email = mongo.db.users.find_one({"username": session["user"]})["email"]
    albums = list(mongo.db.albums.find())
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    str(username)
    first_last = username.split(" ")
    capitalize = [f.capitalize() for f in first_last]
    capitalized_username = " ".join(capitalize)

    if session["user"]:
        return render_template("profile.html", username=username,
                               albums=albums, email=email, count=count,
                               capitalized_username=capitalized_username)

    return redirect(url_for("login"))


@app.route("/albums", methods=["GET", "POST"])
def albums():
    search_query = request.form.get("search")
    search_obj = {}

    if search_query:
        search_obj["$text"] = {"$search": search_query}

    albums = list(mongo.db.albums.find(search_obj))
    genres = list(mongo.db.genres.find())
    return render_template("albums.html", albums=albums, genres=genres)


@app.route("/albums/<album_id>/view")
def view_album(album_id):
    # Gives user access to a page with more info
    # about clicked-on album
    try:
        album = mongo.db.albums.find_one({"_id": ObjectId(album_id)})
        return render_template("view-album.html", album=album)
    except Exception:
        return render_template("404.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    # if User attempts to access upload page
    # while not logged in, they will get
    # redirected to the home page
    if "user" not in session:
        return redirect(url_for('home'))

    current_date = time.strftime("%d-%m-%y")
    if request.method == "POST":
        album = {
            "band_name": request.form.get("band_name"),
            "album_name": request.form.get("album_name"),
            "genre_name": request.form.get("genre_name"),
            "release_date": request.form.get("release_date"),
            "album_image": request.form.get("album_image"),
            "personnel": request.form.get("personnel"),
            "songs": request.form.get("songs"),
            "website": request.form.get("website"),
            "created_by": session['user'],
            "created_at": current_date,
            "rating": request.form.get("rating")}
        mongo.db.albums.insert_one(album)
        flash("Album added to album list")
        return redirect(url_for("albums"))
    numbers = [1, 2, 3, 4, 5]
    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("upload.html", genres=genres, numbers=numbers)


@app.route("/edit/<album_id>", methods=["GET", "POST"])
def edit(album_id):
    # if User attempts to access edit page
    # while not logged in, they will get
    # redirected to the home page
    if "user" not in session:
        return redirect(url_for('home'))

    current_date = time.strftime("%d-%m-%y")
    if request.method == "POST":
        update = {
            "band_name": request.form.get("band_name"),
            "album_name": request.form.get("album_name"),
            "genre_name": request.form.get("genre_name"),
            "release_date": request.form.get("release_date"),
            "album_image": request.form.get("album_image"),
            "personnel": request.form.get("personnel"),
            "songs": request.form.get("songs"),
            "website": request.form.get("website"),
            "created_by": session['user'],
            "created_at": current_date,
            "rating": request.form.get("rating")
        }
        mongo.db.albums.update({"_id": ObjectId(album_id)}, update)
        flash("Album listing updated")
    try:
        album = mongo.db.albums.find_one({"_id": ObjectId(album_id)})
        numbers = [1, 2, 3, 4, 5]
        genres = mongo.db.genres.find().sort("genre_name", 1)
        return render_template("edit.html",
                               album=album, genres=genres, numbers=numbers)
    except Exception:
        return render_template("404.html")


@app.route("/delete/<album_id>")
def delete(album_id):
    # if User attempts to access delete page
    # while not logged in, they will be
    # redirected to the home page
    try:
        mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        return redirect(url_for("home"))

    mongo.db.albums.remove({"_id": ObjectId(album_id)})
    flash("Your listing was removed")
    return redirect(url_for("albums"))


@app.route("/logout")
def logout():
    # if User attempts to access logout page
    # while not logged in, they will be
    # redirected to the home page
    try:
        mongo.db.users.find_one({"username": session["user"]})
    except BaseException:
        return redirect(url_for("home"))

    # Remove user from session cookies
    flash("You are now logged out")
    session.clear()
    return redirect(url_for("login"))


# Throws a custom 404 page if page being searched does not exist
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
