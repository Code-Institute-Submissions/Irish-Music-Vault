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


# Technologies Used
1. randomkeygen.com was used to get a strong password to use as my SECRET_KEY enviornment variable which was needed for use with the flash() and session() functions of Flask. 

# Testing
1. When setting up the flask app in the app.py file, debug is set to true in the app.run method within the 'if __name__ == "__main__":' statement. This is a development procedure that will present a Jinja error screen if there is a bug within a piece of code, and will point me to where in the code the error exists. This was set to false before submission of the project.

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