from flask import Blueprint, render_template, redirect, session

home = Blueprint('home', __name__)

@home.route("/")
def page_home():
    if "username" not in session:
        return redirect("/login")
    else:
        return render_template("/home.html")