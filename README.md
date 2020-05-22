<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

# Python Flask Chat Application

This is a Chat application written in Python and Flask. The purpose of this project is to access data from a URL, and to store the information in a list.

## Heroku Checklist

1. Create a 'requirements.txt' file, from the virtual environment to only load the necessary dependencies: pip3 freeze > requirements.txt

2. Create a 'Procfile': echo web: python3 run.py > Procfile

3. Create a new Heroku application: heroku login (open browser to login) -> heroku apps:create flask-chat-mini-project-gaff
> Creating ⬢ flask-chat-mini-project-gaff... done
>
> https://flask-chat-mini-project-gaff.herokuapp.com/ | https://git.heroku.com/flask-chat-mini-project-gaff.git

4. Create Heroku application configuration variables:

5. Push the code form Git to Heroku: