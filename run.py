import os
from flask import Flask, render_template, request, flash
import json
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/place.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", place=data)


@app.route("/about/<place_name>")
def about_place(place_name):
    place = {}
    with open("data/place.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == place_name:
                place = obj
    return render_template("place.html", place=place)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("thanks {}, we've received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)