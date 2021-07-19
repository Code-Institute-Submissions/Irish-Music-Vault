# @app.route("/search", methods=["GET", "POST"])
# def search():
#    search = request.form.get("search")
#    albums = list(mongo.db.albums.find({"$text": {"$search": search}}))
#    genres = list(mongo.db.genres.find())
#    return render_template("albums.html", albums=albums, genres=genres)



# try:
#        mongo.db.users.find_one({"username": session["user"]})
#    except BaseException:
#        return redirect(url_for("home"))

#album = mongo.db.albums.find_one({"_id": ObjectId(album_id)})
#    return render_template("view-album.html", album=album)
#



# @app.route("/albums", methods=["GET", "POST"])
# def albums():
#    albums = list(mongo.db.albums.find())
#    genres = list(mongo.db.genres.find())
#    return render_template("albums.html", albums=albums, genres=genres, )

#albums = list(mongo.db.albums.find())
#    return render_template("home.html", albums=albums)