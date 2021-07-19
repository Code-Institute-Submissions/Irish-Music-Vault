# @app.route("/search", methods=["GET", "POST"])
# def search():
#    search = request.form.get("search")
#    albums = list(mongo.db.albums.find({"$text": {"$search": search}}))
#    genres = list(mongo.db.genres.find())
#    return render_template("albums.html", albums=albums, genres=genres)









# @app.route("/albums", methods=["GET", "POST"])
# def albums():
#    albums = list(mongo.db.albums.find())
#    genres = list(mongo.db.genres.find())
#    return render_template("albums.html", albums=albums, genres=genres, )