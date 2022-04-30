from flask import Flask, render_template

app = Flask("Flask Web Scrapper")

@app.route("/")
def home():
    return render_template("potato.html")

@app.route("/<username>")
def contact(username):
    return f"Hello {username} how are you doing"

app.run()
