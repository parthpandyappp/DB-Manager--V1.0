from flask import Flask, request, render_template, redirect
import csv
app = Flask(__name__)
students = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registered")
def registered():
    with open("registered.csv", "r") as file :
        reader = csv.reader(file)
        students = list(reader)
       
    return render_template("registered.html", students = students)

@app.route("/register" , methods = ["POST"])
def register():

    if not request.form.get("name") or not request.form.get("Course"):
        return "failure"

    with open("registered.csv", "a") as file :
        writer = csv.writer(file)
        writer.writerow((request.form.get("name"), request.form.get("Course")))
    return redirect("/registered")

