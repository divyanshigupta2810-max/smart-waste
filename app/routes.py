from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("home.html")


@main.route("/login")
def login():
    return "Login page coming soon"


@main.route("/health")
def health():
    return {"status": "ok", "message": "Smart Waste System is running"}