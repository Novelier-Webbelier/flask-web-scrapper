from flask import Flask

app = Flask("Flask Web Scrapper")

@app.route("/")
def home():
    return "<p>Hello! Welcome my website!</p>"

@app.route("/contact")
def contact():
    return "Contact me!"

app.run()
