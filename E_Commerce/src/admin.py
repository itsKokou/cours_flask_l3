# Metier de l'admin
from flask import render_template
from .client import app

@app.route("/admin/home")
def hello_admin():
    return render_template("admin/home.html")
