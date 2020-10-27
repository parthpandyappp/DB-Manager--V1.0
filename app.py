from flask import Flask, request, render_template, redirect
import csv
import os
app = Flask(__name__)
students = []
id =0;

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

    if not request.form.get("name") or not request.form.get("Course") or not request.form.get("email"):
        return "failure"

    with open("registered.csv", "a") as file :
        writer = csv.writer(file)
        writer.writerow((request.form.get("name"), request.form.get("email"), request.form.get("Course")))
    return redirect("/registered")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug="True")