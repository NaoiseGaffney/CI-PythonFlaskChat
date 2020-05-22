import os
from datetime import datetime
from flask import Flask, redirect, request, session, render_template, url_for

app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []

def add_message(username, message):
    """Add messages to the 'messages' list."""
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = {"timestamp": now, "from": username, "message": message}
    message.append(messages_dict)


@app.route("/", methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]
    
    if "username" in session:
        return redirect(url_for("user", username = session["username"]))

    return render_template("index.html")

@app.route("/chat/<username>", methods=["GET", "POST"])
def user(username):
    """Add and display chat message."""
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(session["username"])
        
    return render_template(url_for("user", username=session["username"]))

app.run(host=os.getenv("IP"), port=(os.getenv("PORT")), debug=True)
