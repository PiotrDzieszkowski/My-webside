from flask ifrom flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/message')
def info():
    return render_template("me.html")

@app.route('/about_me', methods=["GET", "POST"])
def about_me():
    if request.method == "GET":
        return render_template("about_me.html")
    elif request.method == "POST":
        print("POST received")
        print(request.form)
        return render_template("about_me.html")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        print("POST received")
        print(request.form)
        return render_template("contact.html")

@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("me.html")
    elif request.method == "POST":
        print("POST received")
        print(request.form)
        return render_template("me.html")