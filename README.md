# About
Irish Music Vault is intended as a database of albums recorded by Irish bands to be updated by both an admin and users of the site. The goal is to, in time, have a fully comprehensive database of albums across a multitude of genres.

# UX
## User Stories:
1. As a visitor to the site, I am looking for a comprehensive database of albums by a diverse genre list of Irish bands.
2. As a visitor to the site, I want to be able to either add my own bands albums and/or another bands albums.
3. As a visitor to the site, I want the database to be easy to navigate and without duplicate albums being present.
4. As a visitor to the site, I want to have my own profile page on which I can clearly see my own uploads and edit/delete them if I so wish. For this I would require the ability to register and login.
5. As a visitor to the site, I want links to online shops wherein I can purchase the listed albums. 
6. As a visitor to the site, I want a search bar with which to easily navigate the albums list. 
7. As a visitor to the site, I want a way to communicate with other users of the site via a comments section. 

# Design
## Fonts
The site uses two fonts. 
1. For the main text on the site within paragraphs and the copyright, Cormorant Garamond is used and taken from Google Fonts. 
2. For headings and the site logo text, Comfortaa is used and taken from Gogle fonts.
## Color palette
1. The bar, footer

# Technologies Used
1. MongoDB was used as a database for holding any data related to the site.  
2. randomkeygen.com was used to get a strong password to use as my SECRET_KEY enviornment variable which was needed for use with the flash() and session() functions of Flask. 
3. Favicon.io was used to design a favicon for the site. (https://favicon.io/favicon-generator/)

# Testing
1. When setting up the flask app in the app.py file, debug was set to true in the app.run method within the 'if __name__ == "__main__":' statement, which is used to instruct the application on which parameters to run flask on by use of enviornment variables. This is a development procedure that will present a Jinja error screen if there is a bug within a piece of code, and will point me to where in the code the error exists. This was set to false before submission of the project.

# Bugs
1. On the albums.html page, when trying to loop over the 'genre_name' key within my 'genres' collection I was unable to use the same 'for loop' twice. This is because the variable 'genres' that I had assigned the 'mongo.db.genres.find()' method to within the app.py file can only 'unpack' the data from the mongoDB database once. This was fixed by enclosing the method within the list() method (i.e. list(mongo.db.genres.find()) ) to convert the returned data into a list object. The data can then be rendered more than once.

# Deployment

## Deployment to Heroku
1. In the command line, 'pip3 freeze --local > requirements.txt' is run in order to set up a requirements.txt file. Heroku uses this to see what dependencies are needed to run the application.
2. A Procfile is created which tells Heroku which Python file is used in order to run the application. The command in the command line interface is 'echo web: python app.py > Procfile'. App.py is a standard naming convention for this type of Python file. Inside this Procfile is 'web: python app.py'.
3. These two files are then pushed to GitHub. Heroku will be running the application via the GitHub repository and so any files needed to run the app should be present there. 'git add -A', 'git commit -m "Add requirements.txt and Procfile"' and 'git push' are used to push these files to GitHub.
4. After setting up an account at heroku.com, on the dashboard I click the button with 'New' written on it, in the top right-hand corner of the screen, and then 'Create new app' from the dropdown menu. On the following page I create the name of my app which is 'Irish-Music-Vault' and click the 'European' option for which region I am in. I then click the 'Create app' button below the two dropdown menus.
5. On the next page which is the dashboard for my project, I click on the GitHub icon which allows me to connect my GitHub account and choose the name of my repository to link to, making sure that the link is being made to my personal GitHub account. Once my repository is found I click on the button with 'connect' written on it. My project is now linked to my Heroku project.                           
6. Next I need to pass my enviornment variables to Heroku. This is necessary as these variables are stored within my env.py file which has been passed to my .gitignore file. This .gitignore file stops whatever files are marked inside it from being pushed to GitHub. The env.py file contains private information such as a password and thus should not be pushed to GitHub where it can be viewed publicly. So, clicking on settings in the horizontal menu near the top of the page and then clicking on the 'Reveal Config Vars' button within the Config Vars section I am now presented with a form in which to write the key, value pairs into, minus any quotation marks around these key, value pairs. 
7. Then, back within the 'Deploy' section of my Heroku profile, and within the 'Automatic Deploys' area, I click on the 'Enable Automatic Deploys' button. 
8. Once Heroku has finished retrieving information from my GitHub repository I am presented with a button with 'View' written on it. This allows me to open up the project in the server.

# Credits
## Photos:
1. Photo of Dogrel by Fontaines D.C. taken from https://www.fiveriserecords.co.uk/wp-content/uploads/2019/02/fontaines-dc-dogrel.jpg
2. Photo of The Dubliners in Concert taken from https://images-na.ssl-images-amazon.com/images/I/61Udja6jyPL.jpg
3. Photo of Zeitgeist by the Kevin Brady Trio taken from https://images.stevesjazzsounds.co.uk/images/products/original/11122009122925_160366280.jpg
4. Photo of The Joshua Tree by U2 taken from https://images.genius.com/9790ce9f55a20d4664a52002b140ed68.1000x1000x1.jpg
5. Photo of Suas Síos by Kíla taken from https://1.bp.blogspot.com/-XkHztxWMDJM/VYwHf1baNJI/AAAAAAAAExg/vB37DgDNu5c/s1600/11156152_10153214442287243_3030651577277183716_n.jpg
6. Photo of Vagabonds of the Western World by Thin Lizzy taken from https://cdn.cdon.com/media-dynamic/images/product/music/vinyllp/image769/vagabonds_of_the_western_world_vin-thin_lizzy-49230935-frntl.JPG
7. Photo of Justin Carroll's Togetherness taken from https://justincarroll.bandcamp.com/album/togetherness
8. Photo of Agreements by Matt Halpin taken from https://matthewhalpinmusic.bandcamp.com/album/agreements
9. Photo of Crazy World by Aslan taken from https://img.discogs.com/xtHtiwsexYZeijXDqFweFUZ1AMU=/fit-in/500x460/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-9590441-1483291962-3233.jpeg.jpg
10. Photo of the Pogues, Waiting For Herb taken from https://en.wikipedia.org/wiki/Waiting_for_Herb#/media/File:Waiting_for_herb.jpg
11. Photo of the Dubliners, Revolution taken from https://en.wikipedia.org/wiki/Revolution_(The_Dubliners_album)#/media/File:Dubliners_Revolution.jpg
12. Photo of Echos by John Moriarty taken from https://www.rte.ie/entertainment/music-reviews/2013/0306/449906-guitar/