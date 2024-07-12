from flask import render_template
from .client import app

@app.route('/admin/home')
def home_a():
    return render_template("admin/home.html")