from flask import Flask, render_template, request

app = Flask("Flask Web Scrapper")

# http://127.0.0.1:5000/
@app.route("/")
def home():
    return render_template("potato.html")

# http://127.0.0.1:5000/<username>
@app.route("/<username>")
def contact(username):
    return f"Your name is {username}"

# http://127.0.0.1:5000/report?job=react
@app.route("/report")
def report():
    word = request.args.get("word")
    return render_template("report.html", searchingBy=word)

app.run()
