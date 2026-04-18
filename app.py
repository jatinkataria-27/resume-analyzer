from flask import Flask, render_template, request, redirect, session, send_file
import os
import json
from utils.parser import extract_text
from utils.matcher import analyze_resumes
from utils.report import generate_report

app = Flask(__name__)
app.secret_key = "secret123"

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -------- LOGIN --------
@app.route("/", methods=["GET","POST"])
def login():
    error = None

    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        with open("database/users.json") as f:
            users = json.load(f)

        if user in users and users[user] == pwd:
            session["user"] = user
            return redirect("/dashboard")
        else:
            error = "Invalid Username or Password"

    return render_template("login.html", error=error)


# -------- DASHBOARD --------
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/")

    if request.method == "POST":
        files = request.files.getlist("resumes")
        jd = request.form["jd"]

        resumes = []
        names = []

        for file in files:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)
            text = extract_text(path)
            resumes.append(text)
            names.append(file.filename)

        results = analyze_resumes(resumes, jd, names)

        session["results"] = results
        return render_template("result.html", results=results, jd=jd)

    return render_template("dashboard.html")


# -------- DOWNLOAD REPORT --------
@app.route("/download")
def download():
    results = session.get("results")
    file_path = generate_report(results)
    return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)