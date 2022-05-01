from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("Flask Web Scrapper")

fake_db = {}

# http://127.0.0.1:5000/
@app.route("/")
def home():
    return render_template("home.html")

# http://127.0.0.1:5000/<username>
@app.route("/<username>")
def contact(username):
    return f"Your name is {username}"

# http://127.0.0.1:5000/report?job=react
@app.route("/report")
def report():
    word = request.args.get("word")

    if word:
        word = word.lower()
        existingJobs = fake_db.get(word)

        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            fake_db[word] = jobs

    else:
        return redirect("/")

    return render_template(
        "report.html",
        searchingBy=word,
        resultsNumber=len(jobs),
        jobs=jobs
    )

# http://127.0.0.1:5000/export?job=react
@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        word = word.lower()
        jobs = fake_db.get(word)

        if not jobs:
            raise Exception()
        return f"Generate CSV for {word}"
    except:
        return redirect("/")

app.run()
